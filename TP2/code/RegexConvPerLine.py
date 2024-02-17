import re

class RegexConv:
    
    def markdown_to_html(markdown_text):
        
        # Não dá para usar carrots (^) ou dollars sign ($) pq ele lê o ficheiro inteiro em vez de linha a linha
        # Faz isso para poder criar a lista mais facilmente
        md = {
            "h1" : re.compile(r'#{1} (.+)'),
            "h1goat" : re.compile(r'(?<!#)#{1}(?!#) (.+)'),
            "h2" : re.compile(r'#{2} (.+)'),
            "h2goat" : re.compile(r'(?<!#)#{2}(?!#) (.+)'),
            "h3" : re.compile(r'#{3} (.+)'),
            "h3goat" : re.compile(r'(?<!#)#{3}(?!#) (.+)'),
            "bold" : re.compile(r'\*{2}(.+)\*{2}'),
            "italic" : re.compile(r'\*(.+)\*'),
            "italicgoat" : re.compile(r'(?<!\*)\*(?![*])([^*]*[^*])\*(?!\*)'),
            "blockquote" : re.compile(r'\n+ *>+(.*)')
            
            
        }
        
        # Converter Títulos
        markdown_text = re.sub(md["h1goat"], r'<h1>\1</h1>', markdown_text)
        markdown_text = re.sub(md["h2goat"], r'<h2>\1</h2>', markdown_text)
        markdown_text = re.sub(md["h3goat"], r'<h3>\1</h3>', markdown_text)
        
        # Converter Negrito e Itálico
        # se for usado o italico simples, tem de ser depois do bold pq captura a mesma sequencia
        markdown_text = re.sub(md["italicgoat"], r'<em>\1</em>', markdown_text)
        markdown_text = re.sub(md["bold"], r'<b>\1</b>', markdown_text)

        # Converter Blockquote
        markdown_text = re.sub(md["blockquote"], r'\n<blockquote>\1</blockquote>', markdown_text)

        
        # Converter Listas

        
        # Converter Código

        
        # Converter Linha Horizontal

        
        # Converter Links

        
        # Converter Imagens

    
        return markdown_text


