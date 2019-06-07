---
layout: post
title: Retrospective
date: '2019-05-22 01:00:00 -07:00'
author: David Vitale
categories: ["blog", "travel", "alaska-roadtrip"]
tags: ["travel", "nature", "roadtrip"] 
modified_time: '2019-05-22 01:00:00 -07:00'
featured: true
---

Two years ago today, I left on a once-in-a-lifetime roadtrip to Alaska with great friends Kevin, Isaac, and Joey. We drove to from Chicago to Alaska and back, stopping at many amazing locations along the way. I took pictures and captured my thoughts [in a blog](/blog/travel/alaska-roadtrip/) along the way, but never wrote a proper retrospective for my trip.

{% leaflet_map {"zoom" : 3,
                "center": [55, -130],
                "esriBasemap" : "Topographic" } %}
    {%- for post in site.posts -%}
        {% if post.location.geojson %}
            {% leaflet_geojson post.location.geojson %}
        {% endif %}
    {% endfor %}
{% endleaflet_map %}

>Each point on the map above represents a stop on our trip 

## South Dakota, Montana

Our first stop was the Badlands in South Dakota, we climbed up some rock formations and saw some wild mountain goats. We then went to the Black Hills in South Dakota, where we saw Mt. Rushmore and some wild bison. We then backpacked in Glacier National Park, where we witnessed unbelievable sites, pristine water, and breathtaking countryside.

{% include travel-img.html src="/assets/personal/alaska-trip-2017/dude-ranch-2.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/travel-glacier-4.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/end-glacier-5.jpg" %}

## Alberta, British Columbia

We then crossed the border and spent a few days in Banff. We originally planned to do Jasper after, but a park ranger convinced us to do Mount Robson instead. I'm so glad we did that, Mount Robson was one of the best unplanned parts of the trip.

{% include travel-img.html src="/assets/personal/alaska-trip-2017/banff-1.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/robson-1.jpg" %}

## Alaska

After driving ~30 hours from Edmonton to Alaska, we had finally arrived in Alaska, where we visited Denali, Wrangell-St. Elias, Exit Glacier, and a few other places. The absolute highlight of the trip for me was our backpacking in Denali. There is no development at all, just raw nature. It was an unreal experience.

{% include travel-img.html src="/assets/personal/alaska-trip-2017/denali-1.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/exit-2.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/wrangell-1.jpg" %}

## Washington State, Oregon, Wyoming

We made our way down to Vancouver Island, some locations in the Pacific Northwest, and finished off in Yellowstone. All amazing stops to finish our trip off with.

{% include travel-img.html src="/assets/personal/alaska-trip-2017/oregon-1.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/yellowstone-2.jpg" %}

{% include travel-img.html src="/assets/personal/alaska-trip-2017/yellowstone-5.jpg" %}

## Reflection

As I reflect on this trip from 2 years ago, I feel very blessed for all I was able to experience with such amazing friends. Kevin, Isaac, and Joey -- thanks so much for sharing this experience with me. Here's to the next trip!
