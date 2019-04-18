$(function(){


    $(document).on('click','#add_btn',function(){

            var name = document.getElementById("provider_name").value;

            var person = document.getElementById("provider_person").value;

            var phone = document.getElementById("provider_phone").value;
    
            var adress = document.getElementById("provider_adress").value;
            
            var param = {
                name: name,
                person: person,
                phone: phone,
                adress: adress  
            };
            $.ajax({
                url: '/goods/index.php/Home/Addprovider/providerAdd',
                type: 'POST',
                dataType: 'json',
                data: param,
                success: function(data){
                    console.log(data);
                    if(data.code == 0){
                        //var index = template('provider_template',data);
                        //$tbody.prepend(index);
                        layer.msg('添加成功',{icon: 1});
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
        layer.confirm('确认删除？', {
            btn: ['是的','取消'] //按钮
        }, function(){
            var param = {
                id: id
            };
            $.ajax({
                url: '/goods/index.php/Home/Listprovider/providerDelete',
                type: 'POST',
                dataType: 'json',
                data: param,
                success: function(data){
                    console.log(data);
                    if(data.code == 0){
                        layer.msg('删除成功', {icon: 1});
                        $tr.remove();
                    }
                },
                error: function(xhr){
                    console.log(xhr);
                }
            });         
        }, function(){
            //layer.msg('取消');
        });
    });

    $(document).on('click','#editprovider',function(){

            var id = document.getElementById("providerid").value;
            var name = document.getElementById("provider_name").value;
            var person = document.getElementById("provider_person").value;
            var phone = document.getElementById("provider_phone").value;
            var adress = document.getElementById("provider_adress").value;
            var param = {
                id: id,
                name: name,
                person: person,
                phone: phone,
                adress: adress
            };
            $.ajax({
                url: '/goods/index.php/Home/Editprovider/providerEdit',
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
