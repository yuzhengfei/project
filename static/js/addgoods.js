$(function(){
		$(document).on('click','#add_btn',function(){
			var name = document.getElementById("name").value;
			var info = document.getElementById("info").value;


			var param = {
                name: name,
				info: info
			};
			$.ajax({
				url: '/goods/index.php/Home/addgoods/goodsAdd',
				type: 'POST',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('添加成功',{icon: 1});						
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
	});

	$(document).on('click','#editgoods',function(){

		    var id = document.getElementById("id").value;
			var name = document.getElementById("name").value;
			var info = document.getElementById("info").value;
			
			var param = {
				id: id,
                name: name,
				info: info
			};
			$.ajax({
				url: '/goods/index.php/Home/Editgoods/goodsEdit',
				type: 'POST',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('修改成功',{icon: 1});						
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
	});

});