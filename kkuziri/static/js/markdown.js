var simplemde = new SimpleMDE({
	toolbar: [
	"bold", "italic", "strikethrough", "|",
	"heading", "heading-smaller", "heading-bigger", "|",
	"code", "quote", "unordered-list", "ordered-list", "clean-block", "|",
	"link", 
	{
		name: "image",
		action: function customFunction(editor){
			
		},
		className: "fa fa-image",
		title: "Insert Image",
	},
	"table", "horizontal-rule", "|",
	"preview", "side-by-side", "fullscreen", "guide"
	]
});
