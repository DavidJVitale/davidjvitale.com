---
layout: post
title: Algonquin, ON
date: '2015-05-15' 
author: David Vitale
categories: ["blog", "travel", "misc", "backpacking"]
tags: ["travel", "misc", "backpacking"]
featured: false
location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"popupContent": "Algonquin Provincial Park"}, 
            "geometry": {
                "type": "Point",
                "coordinates":
                    [-78.568357, 45.542432]
                }
            }]
        }'
---

>_Note_: This post was written retroactively in 2020

{% leaflet_map { "zoom" : 8 } %}
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

<center><h3>My first ever backpacking adventure of my life!</h3></center>

{% include travel-img.html src="/assets/personal/misc-travel/algonquin/algonquin-1.jpg" %}

In the summer of 2015, I did my first ever overnight "backpacking" adventure in Algonquin Provincial Park, Ontario Canada. I had done a lot of car camping as a Boy Scout, but this was the first conscious decision to throw stuff on our backs, walk to some destination in a park, and spend the night. We were very unprepared with crappy supplies, spent much of our time cold and wet, but overall had a blast. And this one trip probably inspired my next proper backpacking trip, which triggered a life of adventure.

{% include travel-img.html src="/assets/personal/misc-travel/algonquin/algonquin-2.jpg" %}

It was a wet day out, and there were many puddles and mud along our trail. We got lost a few times, but eventually found our way to the lake where we were spending the night. We made dinner, and set up our tent. I remember not sleeping very well, probably due to our crappy gear (no insulation, crappy sleeping bag, etc.).

{% include travel-img.html src="/assets/personal/misc-travel/algonquin/algonquin-4.jpg" %}

We woke up the next morning, finished up our loop, and continued on our trip. Looking back, we had horrible gear and no knowledge whatsoever of what we were doing. But we enjoyed ourselves, learned something, and continued to backpack more.
