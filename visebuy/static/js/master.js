$(document).ready(function() {
    $('.MYCLASS').jqzoom({
        showEffect: 'fadein',
        zoomWidth: 355,
        zoomHeight: 300,
        xOffset: 35,
        title: false
    });

    $('#image-search').change(function() {
        $('#filezone p').text("上载中，请稍候...");
        $('#filezone form').css("visibility", "hidden");
        $('#file-search').submit();
    });

    $('#campan').click(function(e) {
        $('#filezone').toggle();
    }).show();

    $('#q').focus(function() {
        $('#search_tips').show();
    });

    $('#q').blur(function() {
        $('#search_tips').hide();
    });

    $("#campan").hover(function() {
        $("#camera_tips").toggle();
    });

    $("#images img, #productslist img, .home-products img, #recommended img, #more_stuffs img").draggable({
        helper: 'clone',
        appendTo: 'body',
        delay: 50,
        zIndex: 2000
    });

    $("#close_file").click(function(e) {
        $("#filezone").toggle();
    });
    
    // set extended duplicate list to be hidden
    $('ul.duplicate_more').css("display", "none");
    
    // toggle to show more duplicate results
    $("#show_more").click(function() {
    	$('ul.duplicate_more').toggle();
    });
    
    // remove default link of 'x' to homepage
    $("#remove_image").attr("href", "javascript:void(0)");
    
    // 'x' to remove searched image and change to text search
    $("#remove_image").click(function() {
    	$("#searched_image_holder").remove();
    	$("#q").width('425px');
    	$("#q").attr("name", "q");
    	$("#text-search").attr("action", "/visebuy/search/create");
    });
    
    // pressing backspace when no text input to remove searched image
    $("#header #q").keydown(function(e) {
    	if (e.which == 8 && $("#q").val().length == 0)
    	{
    		$("#searched_image_holder").remove();
	    	$("#q").width('425px');
	    	$("#q").attr("name", "q");
	    	$("#text-search").attr("action", "/visebuy/search/create");
    	}
    });

    var image_submit = false;

    $("#fdropzone").droppable({
        tolerance: "touch",
        accept: "img",
        activeClass: 'droppable-active',
        hoverClass: 'droppable-hover',
        over: function(ev, ui) {
            $('#dropzone').css("background", "#F9F9F9").css("color", "#AAA");
        },
        out: function(ev, ui) {
            $('#dropzone').css("background", "url(/visebuy/assets/img/top_background.png) repeat-x scroll center bottom #FFFFFF").css("color", "#000");
        },
        activate: function(ev, ui) {
            $('#dropzone').toggle();
        },
        deactivate: function(ev, ui) {
            if (!image_submit) $('#dropzone').toggle();
        },
        drop: function(ev, ui) {
            image_submit = true;
            $('#dropzone p').text("上载中，请稍候...");
            image_id = ui.draggable.attr("data-id");
            if (typeof image_id != 'undefined') {
                window.location.href = "/visebuy/search/create/?id=" + image_id + "&url=" + encodeURIComponent(ui.draggable.attr("src"));
            } else {
                window.location.href = "/visebuy/search/create/?q=" + ui.draggable.attr("src");
            }
        }
    });

    $("ul.tabs").tabs("div.top_list", {
        effect: 'fade'
    });

    $('.pagination, .nojs, #stats').hide();

    did_scroll = false;
    curr_page = $("span.page-links span.active");
    curr_page_link = '';
    next_page = curr_page.next();
    next_page_link = next_page.attr("href");
    page_num = (curr_page.text().length > 0) ? curr_page.text() : 1;
    products = $('#productslist');

    more_pages = (($(curr_page).length > 0) && ($(next_page).length > 0)) ? true: false;
    if (!more_pages && $(products).find('ul').length > 0) $(products).append("<p class='no_more'>已经没有更多的产品了。</p>");

    $(window).scroll(function() {
        did_scroll = true;
    });

    setInterval(function() {
        if (did_scroll && more_pages) {
            curr_page_link = next_page_link;
            fetch_products();
            did_scroll = false;
        }
    }, 250);

    // load 2nd page on ready as 2nd page will fail to load when screen resolution too big
    if (more_pages)
    {
    	curr_page_link = next_page_link;
    	fetch_products(true);
    }

    function fetch_products(force_load) {

        _force_load = typeof force_load !== 'undefined' ? force_load : false;

        if ($(window).scrollTop() >= $(document).height() - $(window).height() - 50 || _force_load) {
            $.ajax({
                url: next_page_link,
                beforeSend: function() {
                    $(products).addClass('loading');
                },
                success: function(data) {
                    products = $('#productslist');
                    next_page_link = $(data).find("span.page-links span.active").next().attr("href");
                    t = $(data).find("#productslist");
                    $(t).find("img").draggable({
                        helper: 'clone',
                        appendTo: 'body',
                        delay: 50,
                        zIndex: 2000
                    });
                    t.find('.nojs').hide();
                    $(products).append($(t).find('h4')).append($(data).find('.display_type')).removeClass('loading').append($(t).find('ul'));
                    if (typeof next_page_link === 'undefined') {
                        more_pages = false;
                        $(products).append("<p class='no_more'>已经没有更多的产品了。</p>");
                    }
                    // set last loaded page to browser url
                    //if (!window.history || !window.history.pushState) return;
                    //return window.history.replaceState({}, document.title, curr_page_link);
                },
                dataType: 'html'
            });
        }
    }

    var ias = $("#filters p img").imgAreaSelect({
        instance: true,
        handles: true,
        onSelectChange: function(image, selection) {
            if (!selection.width || !selection.height)
            return;
            $('#crop_tips input').show();
        },
        onSelectEnd: function(image, selection) {
            $('input[name=x1]').val(selection.x1);
            $('input[name=y1]').val(selection.y1);
            $('input[name=x2]').val(selection.x2);
            $('input[name=y2]').val(selection.y2);
        }
    });
    
    $("#filters p img").load(function() {
      s_w = $("#filters p img").width() - 10;
      s_h = $("#filters p img").height() - 10;
      ias.setSelection(10, 10, s_w, s_h, true);
      ias.setOptions({ show: true });
      ias.update();
      // sometimes .load not triggered, might have something to do with image being loaded from cache,
      // resulting in image finished loading before event has been attached to it
      // adds checking for image finished loading and trigger the load event if so
    }).each(function() {
    	if (this.complete) {
    		$(this).trigger('load');
    	}
    });
    
    $(window).scroll(function(){
        /*$("#meta").css("top",Math.max(-10,35-$(this).scrollTop()));
        $("#filters-opts").css("top",Math.max(1,46-$(this).scrollTop()));*/
        if ($(this).scrollTop() < 300 && ias != undefined) ias.update();
    });

    var currentPosition = 0;
    var slideWidth = 860;
    var slides = $('.slide');
    var numberOfSlides = slides.length;
    $('#slideshow').css('overflow-x', 'hidden');

    slides.wrapAll('<div id="slideInner"></div>').css({
        'float': 'left',
        'width': slideWidth
    });

    $('#slideInner').css('width', slideWidth * numberOfSlides);
    $('#popular_stuffs').prepend('<ul class="control"><li id="leftControl">前一页 | </li><li id="rightControl">下页</li></ul>');

    manageControls(currentPosition);

    $('#rightControl, #leftControl').bind('click', function() {
        currentPosition = ($(this).attr('id') == 'rightControl') ? currentPosition + 1: currentPosition - 1;
        manageControls(currentPosition);
        $('#slideInner').animate({
            'marginLeft': slideWidth * ( - currentPosition)
        });
    });
    
    function manageControls(position) {
        if (position == 0) {
            $('#leftControl').hide()
        }
        else {
            $('#leftControl').show()
        }
        if (position == numberOfSlides - 1) {
            $('#rightControl').hide()
        }
        else {
            $('#rightControl').show()
        }
    }
    
    image_mouseover = false;
    
    $(".slide, .control").hover(function() {
        image_mouseover = !image_mouseover;
    });
    
    (function loop(){
       setTimeout(function(){          
         if (!image_mouseover && currentPosition < numberOfSlides - 1) $("#rightControl").click();
         if (currentPosition < numberOfSlides - 1) loop();
      }, 7400);
    })();    
    
    var f = $("#filters > form");    
    f.find("input, select").click(function () {
        /*var self = this, 
            list = $('#filters-opts ul');
        $.ajax({
            url: f.attr('action'),
            data: f.serialize(),
            success: function(data) {
                next_page_link = $(data).find("span.page-links span.active").next().attr("href");
                products = $('#productslist');
                t = $(data).find("#productslist");                
                $(t).find("img").draggable({
                    helper: 'clone',
                    appendTo: 'body',
                    delay: 50,
                    zIndex: 2000
                });
                t.find('.nojs, .pagination').hide();
                $(products).replaceWith(t);

				// hide selection for selected filter(slide up)
                $(self).parents('div.filters div').slideUp();

                var _classname = $(self).parents('#filters > form > div').attr('id') || "filt";
                
                // if filter is primary or secondary color, remove it to prevent stacking
                if (_classname == 'prim_colour' || _classname == 'sec_colour') 
                    $(list).find('.'+_classname).remove();
                
                //alert(self.value);

				// add to list of selected filters
                if ($(self).val() !== 'csc' && $(self).val() !== 'cpc')                                    
                    $(list).append('<li class="'+_classname+'">'+$(self).val()+'</li>');
                else if ($(self).val() === 'cpc') 
                    $(list).append('<li class="'+_classname+'">#'+$("#primary_picker").val()+'</li>');                
                else if ($(self).val() === 'csc') 
                    $(list).append('<li class="'+_classname+'">#'+$("#secondary_picker").val()+'</li>');                

                //fetch_products(true);                

                if (!window.history || !window.history.pushState) return;
                return window.history.replaceState({}, document.title, f.attr('action') + "?" + f.serialize());
            },
            dataType: "html"
        });*/
       
       document.forms["filter_form"].submit();
    });

    /*$('#filters-opts ul').on('click', 'li', function() {
        $(this).remove();
        f.find(':contains('+$(this).text()+')').parents('div.filters div').slideDown();
        f.find('[value="'+$(this).text()+'"]').prop('checked', false);
        f.find('#' + $(this).prop('class') + ' ul li').each( function (i) {
            $(this).find('label').removeClass('selected');
        });

        //if (!window.history || !window.history.pushState) return;
        //return window.history.replaceState({}, document.title, f.attr('action') + "?" + f.serialize());
        
        document.forms["filter_form"].submit();
        //location.reload();
    });*/

    $('input[name="pc"]').change(function () {        
        $('#prim_colour').find(".selected").removeClass("selected");
        $(this).parent().addClass("selected");
    });

    
    $('input[name="sc"]').change(function () {
        $('#sec_colour').find(".selected").removeClass("selected");
        $(this).parent().addClass("selected");
    });

    /*$('#filters .filters div').each(function() {
        $(this).css('width', $(this).children("ul").length * 95);
    });*/

    $('#primary_picker').colorpicker({  
        size: 14,
        count: 11,
        hide: true
    });  

    $('#secondary_picker').colorpicker({  
        size: 14,
        count: 11,
        hide: true
    });  
});
