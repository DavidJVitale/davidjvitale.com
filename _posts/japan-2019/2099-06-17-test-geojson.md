---
layout: post
title: Test GeoJSON Kyoto Post
date: '2099-06-17'
author: David Vitale
categories: ["blog", "travel", "japan-2019"]
tags: ["travel", "japan-2019"]
location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"popupContent": "Kyoto 1"},
            "geometry": {
                "type": "Point",
                "coordinates":
                    [135.768326, 35.011665]
            }
        }, {
            "type": "Feature",
            "properties": {"popupContent": "Kyoto 2"},
            "geometry": {
                "type": "Point",
                "coordinates":
                    [135.790, 35]
            }
        }, {
            "type": "Feature",
            "properties": {"popupContent": "Kyoto 3"},
            "geometry": {
                "type": "Point",
                "coordinates":
                    [135.760, 35.011]
            }
        }]
    }'


---


{% leaflet_map { "zoom" : 14 } %}
    {% if page.location.geojson %}
        {% assign geojson = page.location.geojson %}
        {% leaflet_geojson {{geojson}} %}
    {% elsif page.location.latitude and page.location.longitude %}
        {% assign popupContent = page.location.popupContent | default: "" %}
        {% leaflet_marker { "latitude" : {{page.location.latitude}},
                            "longitude" : {{page.location.longitude}},
                            "popupContent" : "{{popupContent}}" } %}
    {% endif %}
{% endleaflet_map %}


Test Kyoto post with 1 picture

{% include travel-img.html src="/assets/personal/alaska-trip-2017/dude-ranch-2.jpg" %}
