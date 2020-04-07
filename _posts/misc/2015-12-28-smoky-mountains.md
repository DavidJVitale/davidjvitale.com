---
layout: post
title: Smoky Mountains
date: '2015-12-28' 
author: David Vitale
categories: ["blog", "travel", "misc", "backpacking"]
tags: ["travel", "misc", "backpacking"]
featured: false
location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"popupContent": "Smoky Mountains National Park"}, 
            "geometry": {
                "type": "Point",
                "coordinates":
                    [-83.392172, 35.632795]
                }
            }]
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

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/group.jpg" %}

In the winter of 2015, I did an overnight backpacking adventure in Smoky Mountains National Park. I had just gotten some new gear for Christmas, and was itching to use it in a proper setting. This was the first "legit" backpacking adventure, having learned a lot from our previous overnight adventure.

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/smoky-1.jpg" %}

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/smoky-2.jpg" %}

We spent the first day hiking to our campsite, taking in the sites along the way. The first day was really hot weather, uncharacteristic for December. We got up to our site, filtered some water (first time doing so in my life), and ate some hot dinner. We put our food up on the bear wire and went to sleep in the concrete structure. It got pretty cold in the night, but we were prepared and slept pretty well.

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/smoky-3.jpg" %}

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/smoky-4.jpg" %}

The next day was very rainy with limited visibility. We cut our trip one day short and made it back to civilization by following the Appalacian Trail! It was very cool to hike on part of that famous trail.

When we finished our whole camping part of our trip and got to our hotel, I very selflessly volunteered to "take the first shower to keep things moving". It was a major dick move to sneak a shower in instead of pulling straws for going first like discussed. My friends never let me live it down.

{% include travel-img.html src="/assets/personal/misc-travel/smoky-mountains-1/prep.jpg" %}

This trip holds a very special place in my heart, since I view it as the "legit" start to my life-long journey of backpacking and camping. We had proper gear, did the proper preparation, and were overall pretty prepared. It was a blast, and I can't thank my friends enough for making these memories.
