---
layout: post
title: Northern California Road Trip
date: '2018-09-01 01:00:00 -07:00'
author: David Vitale
categories: ["blog", "travel", "norcal-roadtrip"]
permalink: "/blog/travel/norcal-roadtrip/"
tags: ["travel", "nature", "roadtrip"] 
modified_time: '2019-09-01 01:00:00 -07:00'
location:
    geojson: '{
        "type": "FeatureCollection",
	"features": [{
            "type": "Feature",
   	    "properties": {"popupContent": "Yosemite Valley"},
	    "geometry": {
	        "type": "Point",
	        "coordinates":
                    [-119.576346, 37.740828]
	    }
        }, {
            "type": "Feature",
   	    "properties": {"popupContent": "Crater Lake"},
	    "geometry": {
	        "type": "Point",
	        "coordinates":
                    [-122.106499, 42.941736]
	    }	
	}, {
            "type": "Feature",
   	    "properties": {"popupContent": "The Redwoods"},
	    "geometry": {
	        "type": "Point",
	        "coordinates":
                    [-124.005797, 41.204929]
	    }
	}, {
	    "type": "Feature",
	    "properties": {"popupContent": "Lassen Volcanic National Park"},
	    "geometry": {
	        "type": "Point",
	        "coordinates":
                    [-121.419669, 40.493705]
	    }
        }]
    }'
---

{% leaflet_map { "zoom" : 5 } %}
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


Now that I am a working adult, my travel is sadly constrained by when I can take time off of work. And although I have been doing many amazing weekend trips in Southern California/the U.S. Southwest, I was itching for a longer roadtrip. I scored a Yosemite campsite reservation, talked with some friends, and before I knew it we were on our way for a weeklong roadtrip to Yosemite, Lassen Volcanic, Crater Lake, and Redwoods National Parks! Joining me on this adventure were friends Kathy and Marissa. Isaac and Lacey also joined for a bit during Crater Lake.

## Yosemite

This was my first time in Yosemite, and it definitely did not disappoint! Our first day was spent in the valley, mainly exploring the day hike of Vernal Falls and Nevada Falls. We had perfect weather and perfect visibility, it was a great start to our trip.

{% include travel-img.html src="/assets/personal/norcal-2018/yosemite-1.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/yosemite-2.jpg" %}

Our second day was mainly exploring trails and pull-offs off of the 120. We did a short hike to Elizabeth Lake, where I went for an afternon swim (I couldn't convince Kathy and Marissa to join me, sadly). This might have been the highlight of Yosemite for me: the water was cool, refreshing, and <i>so</i> clean. It felt like I was swimming in literal bottled water, definitely one of the cooler experiences of my life.

{% include travel-img.html src="/assets/personal/norcal-2018/yosemite-3.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/yosemite-4.jpg" %}

## Lassen Volcanic

We stopped for half of day in Lassen Volcanic National Park, which contains some of the best thermals outside of Yellowstone. Sadly, the main Bumpass Hell trail was closed, but we did see a cool boiling mud pit on the side of the road. Not much else to report here.

{% include travel-img.html src="/assets/personal/norcal-2018/lassen-1.jpg" %}


## Crater Lake

This was Kathy and Marissa's first time in Oregon! We had great weather and visibility the first day, which gave us many great panoramic views of the deep blue water. Although you spend all day looking at the same lake from different angles, the view never gets old.

{% include travel-img.html src="/assets/personal/norcal-2018/crater-1.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/crater-2.jpg" %}

As mentioned, Isaac and Lacey joined us for this part of the trip. We had so much fun hanging around while hiking and camping, definitely was a highlight catching up with a good friend :).

## Redwoods

Our last stop was Redwoods National Park. I was expecting to see some pretty large trees, and was not let down. I learned that redwood trees can sprout whole new trees from existing trees, leading to some really cool scenarios where an old tree would fall down, and a new tree would sprout from its carcass. Walks through these forests were awe-inspiring, and made me feel really small.

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-1.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-2.jpg" %}

The Redwoods also have miles of undeveloped coast, which was super cool. We had a great time doing everything from soaking in the awesome views from clifftops to finding sea life in beach tidepools.

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-3.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-4.jpg" %}

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-5.jpg" %}

The favorite picture of my lifetime might have been taken during this trip on the Redwoods coastline. The ranger recommended we stop by this beach to view wild seals and sea lions chilling in the water hunting for fish. It was so cool to watching the wild animals try to catch the trout and salmon in the ocean, that I had to take out my superzoom lens on my camera to get a closer look. I was lucky enough to get a few photos of a sea lion catch a trout and eat it whole! Watching that happen live was so incredible, and I was able to get this amazing photo of that moment.

{% include travel-img.html src="/assets/personal/norcal-2018/redwoods-6.jpg" %}

This was a great trip with great friends, something I will definitely cherish and think of when I am back at work soon. I am so happy that I went, it really couldn't have turned out better! Thanks for the memories :).

You can view all the photos from this trip on my <a href="https://www.flickr.com/photos/150318673@N07/albums">Flickr</a>.
