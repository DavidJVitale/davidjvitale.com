---
layout: post
title: Twenty Lakes Basin, Inyo National Forest
date: '2019-09-01' 
author: David Vitale
categories: ["blog", "travel", "misc", "backpacking"]
tags: ["travel", "misc", "backpacking"]
featured: true

location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"popupContent": "Twenty Lakes Basin Trailhead at Saddlebag Lake"}, 
            "geometry": {
                "type": "Point",
                "coordinates":
                    [-119.270856, 37.965729]
                }
            },]
        }'


---

{% leaflet_map { "zoom" : 7 } %}
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

I spent this long holiday weekend in the Inyo National Forest doing an overnight backpacking adventure. This was Indhu's first time backpacking, and she did great! My dog Nali also came along, who had a blast climbing up rocks and exploring all the smells & open space.

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-1.jpg" %}

This area of Inyo is quota-free, which means you can backpack here last minute even on a busy holiday weekend -- you just need a permit from a ranger station. I highly recommend this area fallback if your walk up permits don't work out, it was an amazing trail.

The loop itself is ~8 miles with little elevation gain, which makes it a great intro loop for backpacking. The trail we did can be found [here](https://www.alltrails.com/trail/us/california/twenty-lakes-basin-loop-trail). You can also extend it by going down and up Lundy Falls, or any of the other connecting trails.

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-2.jpg" %}

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-3.jpg" %}

We got to walk around snow in September, which was pretty cool. The lakes being fed from the snow melt were pristine, with many flowing rivers and waterfalls. We found a really cool spot next to a waterfall to spend the night -- Nothing like falling asleep to the sound of running water.

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-4.jpg" %}

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-5.jpg" %}

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-6.jpg" %}

I'll leave you with something fun. Pillows take up a lot of room in a backpack, so they are often left behind. Luckily I have my own mobile heated pillow!

{% include travel-img.html src="/assets/personal/misc/twenty-lakes/twenty-lakes-7.jpg" %}
