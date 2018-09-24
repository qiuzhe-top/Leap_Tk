// 获取点击的课程然后返回小节
var Section_number = new Object; //小节数量对象
var meaID_number = new Object; //小节ID <> N
var s_number =0; //小节ID <> N >> s
var unit_section = new Object; //{单元ID：[1,2,7,8]}
var section_msg = new Object; //{小节ID： {number:[具体题目ID，2，5，48，5],单选 多选 判断 星级:数量。。。} }
var title_all_list = new Array; //[[id,小节，类型，难度],]
var chek_list //获取所有的chek复选框 》 列表
var expect_title //预计的题目量
var obj_pd = 0
var obj_dx = 0
var obj_dax = 0
var obj_aj1 = 0
var obj_aj2 = 0
var obj_aj3 = 0
var obj_aj4 = 0
var obj_aj5 = 0
var Total = 0;
window.onload=function(){
    value_data =document.getElementById('difficulty_radio').value
    // console.log(value_data)
    For_section(value_data)
}
//初始化变量
    function obj_null(){

        obj_pd = 0
        obj_dx = 0
        obj_dax = 0
        obj_aj1 = 0
        obj_aj2 = 0
        obj_aj3 = 0
        obj_aj4 = 0
        obj_aj5 = 0
        Total = 0
        text2_data = ''
        text1_data = ''
        s_number = 0
        meaID_number = {}
        Total = 0
        check_unit_add_data()
    }
//通过ajax 返回 4 大数据
    function For_section(obj){
            obj_null()
            $('#all_number').html(Total)
            for(var key in Section_number){
                delete Section_number[key];
            }
            console.log('发送book ID:',obj)
            $('#courseID').html('')
            $.ajax({
            url:'/myadmin/For_section',
            type:'POST',
            data:{data:obj},
            beforeSend:function(){
                console.log('发送book ID:',obj,'加载中......')
            },
            complete:function(){
                console.log('发送book ID:',obj,'加载完成')
                chek_list = document.getElementsByName('check_unit')
            },
            success:function(arg){
                for(i in arg.msg){
                    data = JSON.parse(arg.msg[i]);
                    console.log(data)
                    for(j in data){
                        // console.log(j)
                        // console.log("单元》》",j)
                    //     <label class="fancy-checkbox display-inline fancy-checkbox-unit">
                    //     <input name="check_unit" value="{{ x.pk }}" type="checkbox" onclick="Section_number_ajax(this);">
                    //     <span>第一单元</span>
                    //      </label>
                        if(j != 'unitID'){
                            t1 = '<label class="fancy-checkbox display-inline fancy-checkbox-unit">'
                            t2 = '<input name="check_unit" value="' + data['unitID'] + '" type="checkbox" onclick="Section_number_unit_ajax(this);">'
                            t3 = '<span>' + j + '</span></label>'
                            text1_data = '<div class="input-group margin_top_10 unit_checkbox_box"><span class="input-group-addon"> ' + t1 + t2 + t3 + ' </span>'
                            s_number = s_number + 1
                            for(k in data[j]){
                                // console.log("小节ID=",data[j][k].id)
                                // console.log("小节name=",data[j][k].title)
                                Section_number[data[j][k].id] = data[j][k].number
                                meaID_number[data[j][k].id] = s_number
                                s_number = s_number + 1
                                text2_data =  text2_data + '<label class="fancy-checkbox display-inline"><input name="check_unit" value="'+ data[j][k].id +'" type="checkbox" onclick="Section_number_ajax(this);"><span>' + data[j][k].title + '(' + data[j][k].number + ')' +'</span></label>'
                            }
                            $('#courseID').append(text1_data + text2_data + '</div>')
                            text1_data = ''
                            text2_data = ''
                        }
                    }

                }
                unit_section = JSON.parse(arg.unit_section)
                section_msg = JSON.parse(arg.section_msg)
                title_all_list = JSON.parse(arg.title_all_list)
                console.log('{单元ID：[小节ID1，小节ID2...]}',unit_section)
                console.log('小节 题量 信息',section_msg)
                console.log('[{题目ID：{题目基础信息}}]',title_all_list)
        
                // console.log(JSON.parse(arg.section_msg))
                // console.log(JSON.parse(arg.title_all_list))
            }
    })
    } 
//选择小节复选框 
    function Section_number_ajax(obj){

        statistical_number(obj.value,obj.checked)
    }
//单机单元复选框
    function Section_number_unit_ajax(obj){
        data = unit_section[obj.value]
        if(obj.checked){
            // Total+=Section_number[obj.value]
            for(i in data){
                cked_index = meaID_number[data[i]]
                if(chek_list[cked_index].checked){

                }else{
                    statistical_number(chek_list[cked_index].value,true)
                }
                chek_list[cked_index].checked=true
            }
        }else{
            // Total-=Section_number[obj.value]
            for(i in data){
                cked_index = meaID_number[data[i]]
                if(chek_list[cked_index].checked){
                    statistical_number(chek_list[cked_index].value,false)
                }else{
                }
                chek_list[cked_index].checked=false
            }
        }
    }
//更新待选数据
    function statistical_number(value,Boolean){
        if(Boolean){
            Total+=Section_number[value]
            obj_pd += section_msg[value].obj_pd 
            obj_dx += section_msg[value].obj_dx 
            obj_dax += section_msg[value].obj_dax 
            obj_aj1 += section_msg[value].obj_aj1 
            obj_aj2 += section_msg[value].obj_aj2 
            obj_aj3 += section_msg[value].obj_aj3 
            obj_aj4 += section_msg[value].obj_aj4 
            obj_aj5 += section_msg[value].obj_aj5 
        }else{
            Total-=Section_number[value]
            obj_pd -= section_msg[value].obj_pd 
            obj_dx -= section_msg[value].obj_dx 
            obj_dax -= section_msg[value].obj_dax 
            obj_aj1 -= section_msg[value].obj_aj1 
            obj_aj2 -= section_msg[value].obj_aj2 
            obj_aj3 -= section_msg[value].obj_aj3 
            obj_aj4 -= section_msg[value].obj_aj4 
            obj_aj5 -= section_msg[value].obj_aj5
        }
        check_unit_add_data()
    }
//html赋值
    function check_unit_add_data(){

        $('#all_number').html(Total)
        $('#all_obj_dax').html(obj_dax)
        $('#all_obj_dx').html(obj_dx)
        $('#all_obj_pd').html(obj_pd)
        $('#all_obj_aj1').html(obj_aj1)
        $('#all_obj_aj2').html(obj_aj2)
        $('#all_obj_aj3').html(obj_aj3)
        $('#all_obj_aj4').html(obj_aj4)
        $('#all_obj_aj5').html(obj_aj5)
    }
//更新预计题量
    function expect_title_onchange(obj){
        expect_title = obj.value
    }

// 《《《题目算法》》》
// 《《《题目算法》》》
// 《《《题目算法》》》
//全部随机
    function title_algorithm_RND1(All_list,number_s){
        var arr = All_list;
        var result = [];
        var ranNum = number_s;
        for (var i = 0; i < ranNum; i++) {
        var ran = Math.floor(Math.random() * arr.length);
        result.push(arr.splice(ran, 1)[0]);
        };
        return result
    }