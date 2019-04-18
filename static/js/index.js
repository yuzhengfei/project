$(function(){
	$('.submit_btn').click(function(e){
		e.preventDefault();
		var name = $('.name').val();
		var password = $('.password').val();
		if(name == '' || password == ''){
			layer.msg('用户名密码不能为空');
			return;
		}
		$.ajax({
			url: '/goods/index.php/Home/Index/login',
			type: 'POST',
			dataType: 'json',
			data: {
				name: name,
				password: password
			},
			success: function(data){
				console.log(data);
				if(data.code == 0){
					window.location = '/goods/index.php/Home/Index/manage';
				}else{
					layer.msg('用户名或密码错误');
				}
			},
			error: function(xhr){				
				console.log(xhr);
			}
		});
	});

	$(document).on('click','.delete_btn',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('接受 | 拒绝？', {
		  	btn: ['接受','拒绝'] //按钮
		}, function(){
			var param = {
				company_id: id,
				sign_statu: 1,
			};
			$.ajax({
				url: 'http://127.0.0.1:8000/sign/stuSign/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('操作成功', {icon: 1});
						$tr.remove();
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});		  	
		}, function(){
		  	// layer.msg('取消');
			var param = {
				company_id: id,
				sign_statu: 0,
			};
			$.ajax({
				url: 'http://127.0.0.1:8000/sign/stuSign/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('操作成功', {icon: 1});
						$tr.remove();
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		});
	});

	// 学生预选
	$(document).on('click','.stuInfo_btn',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('确定选择该课题？', {
		  	btn: ['是','取消'] //按钮
		}, function(){
			var param = {
				topicId: id,
			};
			$.ajax({
				url: '/student/addTopic/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('选择成功！', {icon: 1});
						window.location = '/student/status/';
					}else {
						layer.msg('已有课题，不能预选！', {icon: 1});
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		});
	});
	// 管理员审核老师课题
$(document).on('click','.check_topic',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('通过审核？', {
		  	btn: ['通过','不通过'] //按钮
		}, function(){
			var param = {
				topicId: id,
				result: 1,
			};
			$.ajax({
				url: '/manager/check/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('审核成功', {icon: 1});
						$tr.remove();
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		  	// layer.msg('取消');
			var param = {
				topicId: id,
				result: 0,
			};
			$.ajax({
				url: '/manager/check/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('审核成功', {icon: 1});
						$tr.remove();
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		});
	});

	// 删除老师
	$(document).on('click','.delete_tea',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('是否删除该老师信息？', {
		  	btn: ['是','取消'] //按钮
		}, function(){
			var param = {
				teaId: id,
			};
			$.ajax({
				url: '/manager/delTea/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('删除成功！', {icon: 1});
						$tr.remove();
					}else {}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		});
	});

// 删除学生
	$(document).on('click','.delete_stu',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('是否删除该学生信息？', {
		  	btn: ['是','取消'] //按钮
		}, function(){
			var param = {
				stuId: id,
			};
			$.ajax({
				url: '/manager/delStu/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('删除成功！', {icon: 1});
						$tr.remove();
					}else {}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		});
	});

	// 删除公告
	$(document).on('click','.delete_not',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('是否删除该公告？', {
		  	btn: ['是','取消'] //按钮
		}, function(){
			var param = {
				noticeId: id,
			};
			$.ajax({
				url: '/manager/delNotice/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('删除成功！', {icon: 1});
						$tr.remove();
					}else {}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		});
	});

	// 老师审核学生
	$(document).on('click','.tea_che',function(){
		var $tr = $(this).parents('tr');
		var id = $tr.attr('data-id');
		layer.confirm('通过审核？', {
		  	btn: ['通过','不通过'] //按钮
		}, function(){
			var param = {
				resulId: id,
				result: 1,
			};
			$.ajax({
				url: '/teacher/teacheck/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('审核成功', {icon: 1});
						$tr.remove();
					}else {
						layer.msg('审核失败!该课题人数已满!', {icon: 1});
						return;
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		}, function(){
		  	// layer.msg('取消');
			var param = {
				resulId: id,
				result: 0,
			};
			$.ajax({
				url: '/teacher/teacheck/',
				type: 'GET',
				dataType: 'json',
				data: param,
				success: function(data){
					console.log(data);
					if(data.code == 0){
						layer.msg('审核成功', {icon: 1});
						$tr.remove();
					}
				},
				error: function(xhr){
					console.log(xhr);
				}
			});
		});
	});


});

