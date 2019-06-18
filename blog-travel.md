---
layout: default
title: Travel Blog
permalink: /blog/travel/
---

{% leaflet_map {"zoom" : 1 } %}
    {%- for post in site.posts -%}
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
    {% endfor %}
{% endleaflet_map %}

Click on any point in the above map to read about where I've travelled to!

{% include post-list-by-category.html category="travel" %}
