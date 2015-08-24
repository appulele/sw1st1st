function mousePopUp(node){
  document.getElementById("pupUpText").innerHTML="name:"+node.split("#")[0]+"<br/> Email:"+node.split("#")[2]; 
//$("#pupUpText").attr("innerHTML",node.split("#")[0]);
    $("#pupUpImage").attr("src",node.split("#")[1]+"?type=normal");
    $('#mousePopUp').css({
        "display":"block"
    });
}

function mousePopUphidden(){
    $('#mousePopUp').css({
        "display":"none"
    });
    
}

jQuery(document).ready(function(){
   $(document).mousemove(function(e){
      $('#mousePopUp').css({
            "position" : "absolute",
            "top" : e.pageY-50,
            "left" : e.pageX-100
        });
   }); 
});


(function chart1() {
  var width = 1000,
      height = 1000;

  var color = d3.scale.category20();

  var fisheye = d3.fisheye.circular();
      //.radius(120);

  var force = d3.layout.force()
      .size([width, height])
    .linkStrength(0)
    .friction(0.5)
    .linkDistance(20)
    .charge(0)
    .gravity(0)
    .theta(0.8)
    .alpha(0.1);

  var svg = d3.select("#chart1").append("svg")
      .attr("width", width)
      .attr("height", height);

  svg.append("rect")
      .attr("class", "background")
      .attr("width", width)
      .attr("height", height);

  d3.json("data.json", function(data) {
    var n = data.nodes.length;

    force.nodes(data.nodes).links(data.links);
      
    var radius = 1;
    var layer = 1;
    var num = 0;
      
	var layerNum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
    var layerMaxNum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    var layerMax=0;
      
    data.nodes.forEach(function(d,i){
        if(d.level>0){
            layerMaxNum[d.level]++;
			if(d.level>layerMax){
				layerMax=d.level;
			}
        }
    });
	 
    // Initialize the positions deterministically, for better results.
    data.nodes.forEach(function(d, i) {
        if(d.level>-1){
            layerNum[d.level]++;
            d.x=Math.cos(2*Math.PI/(layerMaxNum[d.level])*layerNum[d.level])*d.level*20;
            d.y=Math.sin(2*Math.PI/(layerMaxNum[d.level])*layerNum[d.level])*d.level*20;
        }else{    
			radius=layerMax;
            //alert(radius);
            if(num<=radius*radius){
                num++;
                d.x=Math.cos(2*Math.PI/(radius*radius)*num)*radius*20;
                d.y=Math.sin(2*Math.PI/(radius*radius)*num)*radius*20;
                //alert(radius);
            }else{
                layerMax++;
                num=0;
            }  
        }
    });
        
        
        
       // d.x=Math.cos(Math.PI/180*i*10)*i*20;  d.y = Math.sin(Math.PI/180*i*10)*i*20; });

    // Run the layout a fixed number of times.
    // The ideal number of times scales with graph complexity.
    // Of course, don't run too long—you'll hang the page!
    force.start();
    for (var i = n; i > 0; --i) force.tick();
    force.stop();

      
    // Center the nodes in the middle.
    var ox = 0, oy = 0;
    data.nodes.forEach(function(d) { ox += d.x, oy += d.y; });
    ox = ox / n - width / 2, oy = oy / n - height / 2;
    data.nodes.forEach(function(d) { d.x -= ox, d.y -= oy; });

    var link = svg.selectAll(".link")
        .data(data.links)
      .enter().append("line")
        .attr("class", "link")
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; })
        .style("stroke-width", function(d) { return Math.sqrt(d.value); });

    var node = svg.selectAll(".node")
        .data(data.nodes)
        .enter().append("circle")
        .attr("class", "node")
        .attr("id",function(d) {return d.user_id })
        .attr("value", function(d) {return d.name})
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("r", 4.5)
        .attr("onmouseenter",function(d) {return "mousePopUp('"+d.name+"#"+d.fb_img+"#"+d.email+"')"})
        .attr("onmouseleave","mousePopUphidden()")
        .style("fill", function(d) { return color(d.group); })
        .call(force.drag);

    svg.on("mousemove", function() {
      fisheye.focus(d3.mouse(this));

      node.each(function(d) { d.fisheye = fisheye(d); })
          .attr("cx", function(d) { return d.fisheye.x; })
          .attr("cy", function(d) { return d.fisheye.y; })
          .attr("r", function(d) { return d.fisheye.z * 4.5; });

      link.attr("x1", function(d) { return d.source.fisheye.x; })
          .attr("y1", function(d) { return d.source.fisheye.y; })
          .attr("x2", function(d) { return d.target.fisheye.x; })
          .attr("y2", function(d) { return d.target.fisheye.y; });
    });
  });
})();