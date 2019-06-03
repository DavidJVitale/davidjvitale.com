module Jekyll
  class RenderTimeTagBlock < Liquid::Block

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    def render(context)
        text = super
        preparsed_html_file_str = File.read("./_plugins/leaflet-map.html")
        parsed_html = preparsed_html_file_str % {inside_block_text: text }
        parsed_html
    end

  end
end

Liquid::Template.register_tag('leaflet_map', Jekyll::RenderTimeTagBlock)
