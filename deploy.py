#!/usr/bin/python3
"""
Builds Jekyll site, syncs to aws s3 bucket without extensions, invalidates
Cloudfront. Can be run both interactively and through a CircleCI CI/CD system
"""

import sys
import subprocess
import os
import shutil
import glob

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
SITE_DIR = os.path.join(ROOT_DIR, "_site")
DEPLOY_DIR = os.path.join(ROOT_DIR, "_deploy")

def main():
    # Initialize and build jekyll
    output_code = 0
    output_code += build_jekyll()
    if output_code != 0:
        return output_code

    # Sync s3 bucket from jekyll build
    if 's3_bucket' in os.environ:
        bucket_name = os.environ['s3_bucket']
        output_code += deploy_to_s3_without_html_extensions(bucket_name)
    else:
        bucket_name = input("Please enter s3 bucket name: ")
        response = input("Sync s3 bucket from jekyll build? (y/n)")
        if 'y' in response:
            output_code += deploy_to_s3_without_html_extensions(bucket_name)
    if output_code != 0:
        return output_code

    # Invalidate cloudfront to update actual site
    if 'cloudfront_distribution_id' in os.environ:
        dist_id = os.environ['cloudfront_distribution_id']
        output_code += invalidate_cloudfront(dist_id)
    else:
        response = input("Invalidate Cloudfront? (y/n) ")
        if 'y' in response:
            try:
                from _cloudfront_mappings import cloudfront_mappings
                dist_id = cloudfront_mappings[bucket_name]
                output_code += invalidate_cloudfront(dist_id)
            except Exception:
                dist_id = input("Enter Cloudfront Distribution ID: ")
                output_code += invalidate_cloudfront(dist_id)

    if os.path.exists(DEPLOY_DIR):
        shutil.rmtree(DEPLOY_DIR)
    
    return output_code

def build_jekyll():
    return run_shell_command(f"cd {ROOT_DIR} && jekyll build")

def deploy_to_s3_without_html_extensions(bucket_name):
        output_code = 0
        if os.path.exists(DEPLOY_DIR):
            shutil.rmtree(DEPLOY_DIR)
        shutil.copytree(SITE_DIR, DEPLOY_DIR)

        for path in glob.glob(os.path.join(DEPLOY_DIR, "blog", "**", "*.html"),
                               recursive=True):
            if 'index.html' in path:
                continue
            path_no_ext_dir = os.path.splitext(path)[0]
            os.mkdir(path_no_ext_dir)
            no_ext_index = os.path.join(path_no_ext_dir, "index.html")
            os.rename(path, no_ext_index)

        output_code += run_shell_command(
            f'aws s3 sync --delete {DEPLOY_DIR} s3://{bucket_name}')
        output_code += run_shell_command(
            f'aws s3 cp "{os.path.join(DEPLOY_DIR, "blog"}" '\
            f's3://{bucket_name}/blogi--recursive --content-type "text/html"')
        return output_code

def invalidate_cloudfront(dist_id):
    return run_shell_command(
            f"aws cloudfront create-invalidation " + \
            f"--distribution-id {dist_id} " + \
            f"--paths '/*'")

def run_shell_command(cmd):
    try:
        print("Currently running command '{}'".format(cmd))
        byte_output = subprocess.check_output(cmd,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
        str_output = byte_output.decode("utf-8")
        print(f"output of command: {str_output}\n-----")
        return 0
    except subprocess.CalledProcessError as e:
        print("cmd failed, returned non-zero code. Output:\n"\
                 "{}".format(e.output.decode("utf-8")))
        return -1

if __name__ == "__main__":
    sys.exit(main())
