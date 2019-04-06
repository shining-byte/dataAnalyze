/**
 *
 * @authors Your Name (you@example.org)
 * @date    2015-07-07 17:52:32
 * @version $Id$
 */
 $(function(){
 	//top层鼠标经过事件
 	$(".quick-menu").children().hover(function(){
 		$(this).addClass('menuhover').find('.menu-bd').show();
 		$(this).find('.hline').hide();
 	},function(){
 		$(this).removeClass('menuhover').find('.menu-bd').hide();
 		$(this).find('.hline').show();
 	});
//分类菜单
var liH=$(".dd ul li").height();
$(".dd ul li").hover(function(){
	$(this).addClass("lihover");
	var	litop=$(this).index()*liH;
	$(this).find(".item-sub").css({display:"block",top:-litop+"px"});
},function(){
	$(this).removeClass("lihover");
	$(".item-sub").css("display","none");
});

//轮播图
var linum=$(".slider li").length;
var liwidth=$(".slider li").width();
$(".slider").css("width",linum*liwidth);

var i=0;
function autoplay(){
	if(i<linum-1){i++;}else{i=0;}
	$(".slider").animate({"left":-liwidth*i+"px"},500);
	$(".dot li").eq(i).addClass("cur").siblings().removeClass("cur");
}
function autoplayprev(){
	if(i<=0){i=4;}else{i--;}
	$(".slider").animate({"left":-liwidth*i+"px"},500);
	$(".dot li").eq(i).addClass("cur").siblings().removeClass("cur");
}
//鼠标经过前进后退按钮，按钮显示与隐藏
$(".flex").hover(function(){
	$(".btn").css("display","block");
	clearInterval(set);
},function(){
	$(".btn").css("display","none");
	set=setInterval(autoplay,5000);
})

$(".btn .prev").click(function(){
	if(!$(".slider").is(":animated")){
		autoplayprev();
	}
})
$(".btn .next").click(function(){
	if(!$(".slider").is(":animated")){
		autoplay();
	}
})
//点击小圆点当前小圆点变为黄色，图片轮播
$(".dot li").click(function(){
	var x=$(this).index();
	i=x;
	$(".slider").animate({"left":-liwidth*i+"px"},2000);
	$(".dot li").eq(i).addClass("cur").siblings().removeClass("cur");

});
var set= setInterval(autoplay,3000);//轮播图

	//每层tab选项卡
	function tab(tabTit,on,tabCon){
		$(tabTit).children().hover(function(){
			$(this).addClass(on).siblings().removeClass(on);
			var index=$(tabTit).children().index(this);
			$(tabCon).children().eq(index).show().siblings().hide();
		});
	}
	tab(".tab","lihover",".main");
});

	//留言评论列表向上滚动
	$(function(){
		var h=$(".sharebox ul li").height()+34;
		var n=$(".sharebox ul li").length;
		var i=0;
		function rolltop(){
			if(i<n-2){i++;
				$(".sharebox ul").animate({top:-h*i},"slow");
			}else{
				$(".sharebox ul").css("top",0);
				i=0;
			}
		}

		setInterval(rolltop,2000);

	})