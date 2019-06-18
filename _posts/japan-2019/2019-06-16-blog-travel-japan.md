---
layout: post
title: Japan & South Korea Trip
permalink: /blog/travel/japan-2019/
tags: ["travel", "japan-2019"]
featured: True
---

{% leaflet_map {"center" : [38, 137],
                "zoom" : 4 } %}
    {%- for post in site.posts -%}
        {% if post.tags contains "japan-2019" %}
            {% if post.location.geojson %}
                {% assign geojson = post.location.geojson | override_hrefs: post.permalink %}
                {% leaflet_geojson {{geojson}} %}
            {% elsif post.location.latitude and post.location.longitude %}
                {% leaflet_marker { "latitude" : {{post.location.latitude}},
                                    "longitude" : {{post.location.longitude}},
                                    "popupContent" : {{post.location.popupContent}},
                                    "href" : "{{post.permalink}}" } %}

            {% endif %}
        {% endif %}
    {% endfor %}
{% endleaflet_map %}

In June of 2019 I travelled to Japan with members of my family. Click any point on the above map to see where we are, or see the posts below!
