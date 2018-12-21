/*
1. 轮播图:
	1. 获取所有图片标签
	2. 每隔一秒切换(变更下标, 取图片元素, 控制显示与隐藏)
	var imgs;
	var imgIndex = 0;
	setInterval()
	function(){
		imgIndex ++;
		imgIndex对应的元素时显示的, 其他的隐藏
		下标越界判断
	}
2. 轮播图下标
	显示在图片上方
*/



/*图片轮播*/
/*等待文档加载完毕后执行function*/
$(function(){
	var imgIndex = 0; //图片下标
	var timerId; //保存定时器ID
	timerId = setInterval(autoPlay,1000); //开启定时器
	//定时器方法,每隔一秒执行一次
	function autoPlay(){
		// 获取图片,根据下标设置元素显示与隐藏
		$('.banner img').eq(imgIndex).css("display","none")
		//更新下标, 防止越界
		imgIndex = ++imgIndex == $(".banner img").length ? 0 : imgIndex;
		//显示下一张图片
		$(".banner img").eq(imgIndex).css("display","block")
		//将所有的图片索引更改为默认颜色
		$(".imgNav li").each(function(){
			//遍历数组, 对每个元素修改背景色
			//this指代当前对象
			$(this).css("background","#CCCCCC")
		});
		
		//切换下标(变更背景颜色)
		$(".imgNav li").eq(imgIndex).css("background","red")
	}
	/*鼠标移入(关闭定时器)移除(重新自动播放)操作*/
	$(".banner").mouseover(function()
	{
		clearInterval(timerId)
	});
	$(".banner").mouseout(function()
	{
		timerId = setInterval(autoPlay,1000);
	});
	$(".imgNav li").each(function()
	{//遍历li元素,为每个元素添加点击事件
		$(this).click(function()
		{//接收到点击
			//点击切换时, 停止定时器
			clearInterval(timerId);
			$(this).css("background","red").siblings().css("background","#CCCCCC");
			//index()获取当前被点击元素的下标
			var index = $(this).index();
			$(".banner img").eq(index).css("display","block").siblings().css("display","none")
			//修改图片下标
			imgIndex = index;
			//点击切换完成之后, 开启定时器
			timerId = setInterval(autoPlay,1000);
		})
	});
}); 
