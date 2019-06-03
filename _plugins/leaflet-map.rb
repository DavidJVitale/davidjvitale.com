module Jekyll
  class RenderTimeTagBlock < Liquid::Block

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    def render(context)
        text = super
        
        leaflet_providers_js_content = File.read("./_plugins/leaflet-providers.js")
        leaflet_loader_js_preparsed = File.read("./_plugins/leaflet-loader.js")
        leaflet_loader_js_parsed = leaflet_loader_js_preparsed % {leaflet_providers_js_content: leaflet_providers_js_content}

        map_preparsed_html = File.read("./_plugins/leaflet-map.html")
        map_parsed_html = map_preparsed_html % {inside_block_text: text,
                                                leaflet_loader_js_content: leaflet_loader_js_parsed}
        map_parsed_html
    end

  end
end

Liquid::Template.register_tag('leaflet_map', Jekyll::RenderTimeTagBlock)
