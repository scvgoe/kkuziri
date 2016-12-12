var simplemde = new SimpleMDE({
	toolbar: [
	"bold", "italic", "|",
	"heading", "heading-smaller", "heading-bigger", "|",
	"code", "quote", "unordered-list", "ordered-list", "clean-block", "strikethrough", "|",
	"link",
	{
		name: "image",
		action: function customFunction(editor){
			$.FileDialog({multiple: false}).on('files.bs.filedialog', function(ev) {
				var files = ev.files;
				var text = "";
				files.forEach(function(f) {
					text += f.name + "<br/>";
				});
				$("#output").html(text);
				
				var fd = new FormData();    
				fd.append( 'file', files[0] );

				$.ajax({
					url: 'http://local.kkuziri.io:5000/image',
					data: fd,
					processData: false,
					contentType: false,
					type: 'POST',
					success: function(data){
						var cm = editor.codemirror;
						var stat = editor.getState(cm);
						var options = editor.options;
						var url = "http://" + data.image_url;

						if(/editor-preview-active/.test(cm.getWrapperElement().lastChild.className))
							return;

						var text;
						var start = options.insertTexts.image[0];
						var end = options.insertTexts.image[1];
						var startPoint = cm.getCursor("start");
						var endPoint = cm.getCursor("end");
						if(url) {
							end = end.replace("#url#", url);
						}
						if(stat.image) {
							text = cm.getLine(startPoint.line);
							start = text.slice(0, startPoint.ch);
							end = text.slice(startPoint.ch);
							cm.replaceRange(start + end, {
								line: startPoint.line,
								ch: 0
							});
						} else {
							text = cm.getSelection();
							cm.replaceSelection(start + text + end);

							startPoint.ch += start.length;
							if(startPoint !== endPoint) {
								endPoint.ch += start.length;
							}
						}
						cm.setSelection(startPoint, endPoint);
						cm.focus();
					}
				});
			}).on('cancel.bs.filedialog', function(ev) {
				$("#output").html("Cancelled!");
			});
		},
		className: "fa fa-image",
		title: "Insert Image",
	},
	"horizontal-rule", "|",
	"preview", "side-by-side", "fullscreen", "guide"
	]
});
