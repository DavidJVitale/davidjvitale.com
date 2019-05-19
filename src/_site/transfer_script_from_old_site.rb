# Disclaimer: I don't know anything about ruby and have hacked this together.
# Mostly followed these pages:
# https://import.jekyllrb.com/docs/blogger/
# https://support.google.com/blogger/answer/41387?visit_id=636938223500161719-1704480691&rd=1

require "jekyll-import";
    JekyllImport::Importers::Blogger.run({
      "source"                => "/path/to/blog-05-18-2019.xml",
      "no-blogger-info"       => false, # not to leave blogger-URL info (id and old URL) in the front matter
      "replace-internal-link" => false, # replace internal links using the post_url liquid tag.
    })
