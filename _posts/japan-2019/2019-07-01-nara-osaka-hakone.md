---
layout: post
title: Nara, Osaka, Hakone
date: '2019-07-01' 
author: David Vitale
categories: ["blog", "travel", "japan-2019"]
tags: ["travel", "japan-2019"]

location:
    geojson: '{
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"popupContent": "奈良市 (Nara)" },
            "geometry": {
                "type": "Point",
                "coordinates":
                    [135.805, 34.6851]
            }
        }, {
            "type": "Feature",
            "properties": {"popupContent": "箱根町 (Hakone)"},
            "geometry": {
                "type": "Point",
                "coordinates":
                    [139.0132, 35.1214] 
            }
        }, {
            "type": "Feature",
            "properties": {"popupContent": "大阪市 (Osaka)"}, 
            "geometry": {
                "type": "Point",
                "coordinates":
                   [135.308, 34.3148] 
            }
        }
      ]
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

Tokyo and Kyoto have been our main Japanese stops on this trip. But we have also done day trips or half day trips to Nara, Osaka, and Hakone. These are the highlights from each of those locations. 

{% include travel-img.html src="/assets/personal/japan-2019/group-photo-5.jpg" %}


## Nara 

Nara is a very bizarre place, mainly because of the deer. They are very domesticated (and chubby) because tourists like to feed them cookies. You approach them, they beg for food by bowing at you, and you pet them. They will walk around with you and just sort of hang out.

{% include travel-img.html src="/assets/personal/japan-2019/deer-1.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/deer-2.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/deer-3.jpg" %}

We also went to 東大寺 (Tōdai-ji), an ancient (8th century!) Buddhist temple in Nara. The bronze Buddha was humongous, it was crazy to think something that large could have been constructed that long ago. Here is a picture of me for scale.

{% include travel-img.html src="/assets/personal/japan-2019/temple-5.jpg" %}

## Osaka 

We only had half a day here but we got some more 蛸焼 (Takoyaki) and お好み焼き (Okonomiyaki) from the Kuromon Market. These foods are famous to get in Osaka, and they did not dissapoint. So savory and greasy, definitely "soul food". 

{% include travel-img.html src="/assets/personal/japan-2019/street-food-3.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/street-food-4.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/street-food-5.jpg" %}

Other foods tried: grilled octopus, grilled scallops, some red-bean rice cake with strawberry, crab sticks, other things. Everything is served on a stick or grilled and it is all delicious. 

## Hakone 

We spent one day in Hakone, a beautiful, quiet town outside of Tokyo. We weren't brave enough to embrace the full nudity onsens, instead opting for shopping and sight-seeing. The clouds blocked our view of Mt Fuji but it was still a great day! We went to the 箱根神社 (Hakone Shrine). 

{% include travel-img.html src="/assets/personal/japan-2019/temple-6.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/temple-7.jpg" %}

{% include travel-img.html src="/assets/personal/japan-2019/temple-8.jpg" %}

## Onto Korea!

We now spend 3-4 days in Seoul before flying back. Looking forward to the sight-seeing and delicious food!
