---
layout: post
title: Japan & South Korea Trip
permalink: /blog/travel/japan-2019/
categories: ["travel", "japan-2019"]
tags: ["travel", "japan-2019"]
featured: True
---

{% leaflet_map {"center" : [38, 137],
                "zoom" : 4 } %}
    {%- for post in site.posts -%}
        {% if post.categories contains "japan-2019" %}
            {% if post.location.geojson %}
                {% assign geojson = post.location.geojson | override_hrefs: post.url %}
                {% leaflet_geojson {{geojson}} %}
            {% elsif post.location.latitude and post.location.longitude %}
                {% assign popupContent = post.location.popupContent | default: "" %}
                {% assign href = post.url | default "" %}
                {% leaflet_marker { "latitude" : {{post.location.latitude}},
                                    "longitude" : {{post.location.longitude}},
                                    "popupContent" : "{{popupContent}}",
                                    "href" : "{{href}}" } %}
            {% endif %}

        {% endif %}
    {% endfor %}
{% endleaflet_map %}

Today I travel to Japan and South Korea with members of my family. I will write blog posts for each of our destinations -- to see where we are, click a marker in the above map or one of the links below!

{% include post-list-by-category.html category="japan-2019" %}
