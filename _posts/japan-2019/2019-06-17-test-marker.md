---
layout: post
title: Sample Test Tokyo Post
date: '2019-06-17'
author: David Vitale
categories: ["blog", "travel", "japan-2019"]
tags: ["travel", "japan-2019"]
location:
    latitude: 35.652832
    longitude: 139.839478
    popupContent: "Hello Tokyo!"
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

Sample Tokyo post with 1 picture

{% include travel-img.html src="/assets/personal/alaska-trip-2017/dude-ranch-2.jpg" %}
