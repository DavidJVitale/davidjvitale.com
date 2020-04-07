---
layout: post
title: Mammoth Cave, KY
date: '2015-08-10' 
author: David Vitale
categories: ["blog", "travel", "misc"]
tags: ["travel", "misc",]
featured: false
location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [
            {
            "type": "Feature",
            "properties": {"popupContent": "Mammoth Cave National Park"}, 
            "geometry": {
                "type": "Point",
                "coordinates":
                    [-86.100035, 37.187214]
                }
            }
        ]
    }'

---

>_Note_: This post was written retroactively in 2020

{% leaflet_map { "zoom" : 11 } %}
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

{% include travel-img.html src="/assets/personal/misc-travel/mammoth-1.jpg" caption="Left to right: Joey, Kevin, Caroline, Dan, David" %}

In the summer of 2015, I got to go spelunking in Mammoth Cave National Park, Kentucky. I highly recommend visiting this place -- they have many cave tours of all levels. We skipped all the baby tours and went straight for the most intense "Wild Cave Tour".

It was such a one-of-a-kind experience. You're crawling through small cave openings, jumping across gaps, and squeezing through rocks. Your headlight illuminates the person in front of you and your immediate surroundings as you navigate through a maze of tunnels, experiencing firsthand the effects water + time has on the rocks in a cave. There were so many amazing rock formations, delicate ecosystems, humongous rooms. This place is awesome.

Also, shoutout to Joey for keeping his cool when I accidentally spilled a whole water bottle over his sandwich for lunch.
