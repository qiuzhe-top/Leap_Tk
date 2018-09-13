var ajax_data = new Array();
window.onload = function () {
    // 自动加载
    subject_types()
    data =  $('#Book').find("option")[0].value
    // console.log(data)
    Book_value(data)

}
// 显示隐藏功能
    function subject_types() {
        a = $('#subject_types').val()
        if (a == "单选") {
            shou_radio()
        } else if (a == "多选") {
            shou_check()
        } else if (a == "判断") {
            shou_if()
        }
    }

    function shou_radio() {
        $('#radio_box').show();
        $('#answer_radio_box').show();
        $('#checkbox_box').hide();
        $("#if_box").hide();
        $("#answer_checkbox_box").hide();
    }

    function shou_check() {
        $('#radio_box').show();
        $('#answer_checkbox_box').show();
        $('#checkbox_box').show();
        $("#if_box").hide();
        $("#answer_radio_box").hide();
    }

    function shou_if() {
        $('#radio_box').hide();
        $('#checkbox_box').hide();
        $("#if_box").show();
    }



//提交题目 到服务器
    function subject_form_ajax() {
        data = ''
        // 题目
        subject = CKEDITOR.instances['id_subject_form'].getData(); //获取富文本值
        // subject=subject.ToString().RTrim('')     
        subject = subject.substr(0, subject.length - 1);
        subjectlen = subject.length


        //答案
        Answer_subject()
        // 题目信息
        subject_information()
        // 选项
        text_subject()

        data = String(ajax_data)
        console.log(data)

        $.ajax({
            url: '/myadmin/add',
            type: 'POST',
            data: {
                data: data,
                subject: subject
            },
            success: function (arg) {
                // bounceInUp(arg.SMS)
                console.log(arg.msg)
                toastbackground(arg.msg)

            }
        })
        for (var key in ajax_data) {
            delete ajax_data[key];
        }
    }
    // 获取题目答案
    function Answer_subject() {
        a = $('#subject_types').val()
        if (a == "单选") {
            ajax_data[3] = $('#answer_radio').val()
        } else if (a == "多选") {
            ajax_data[3] = Answer_check()
        } else if (a == "判断") {
            ajax_data[3] = $("input[name='gender']:checked").attr('value');
        }
    }
    // 获取多选框答案
    function Answer_check() {
        var categoryList = "";
        $('input:checkbox[name=check_answer]:checked').each(function (i) {
            if (0 == i) {
                categoryList = $(this).val();
            } else {
                categoryList += $(this).val();
            }
        });
        return categoryList
    }
    // 获取题目分类详细信息
    function subject_information() {
        ajax_data[1] = $('#minutia').val()
        ajax_data[2] = $('#subject_types').val()
    }
    // 获取题目选项内容
    function text_subject() {
        text = ''
        a = $('#subject_types').val()
        if (a == "单选") {
            ajax_data[4] = $('#answerA').val()
            ajax_data[5] = $('#answerB').val()
            ajax_data[6] = $('#answerC').val()
            ajax_data[7] = $('#answerD').val()
        } else if (a == "多选") {
            ajax_data[4] = $('#answerA').val()
            ajax_data[5] = $('#answerB').val()
            ajax_data[6] = $('#answerC').val()
            ajax_data[7] = $('#answerD').val()
            ajax_data[8] = $('#answerE').val()
            ajax_data[9] = $('#answerF').val()
        }
    }



// 选择书本单元小节
    // 手动 书本
    function Book_onchange(obj) {
        a = obj.value
        $.ajax({
            url: '/myadmin/getunit',
            type: 'POST',
            data: {
                data: a
            },
            success: function (arg) {
                data = JSON.parse(arg.data);
                $('#Unit').html("")
                for (i = 0; i < data.length; i++) {
                    text = "<option value='" + data[i]['id'] + "'>" + data[i]['title'] + "</option>"
                    // console.log(text)
                    $('#Unit').append(text)
                }
            }
        })
    }
    // 自动 书本
    function Book_value(data){
        $.ajax({
            url: '/myadmin/getunit',
            type: 'POST',
            data: {
                data: data
            },
            success: function (arg) {
                data = JSON.parse(arg.data);
                $('#Unit').html("")
                for (i = 0; i < data.length; i++) {
                    text = "<option value='" + data[i]['id'] + "'>" + data[i]['title'] + "</option>"
                    // console.log(text)
                    $('#Unit').append(text)
                }
            }
        })
    }
    // 手动  单元
    function Unit_onchange(obj) {
        a = obj.value
        $.ajax({
            url: '/myadmin/getminutia',
            type: 'POST',
            data: {
                data: a
            },
            success: function (arg) {
                data = JSON.parse(arg.data);
                $('#minutia').html("")
                for (i = 0; i < data.length; i++) {
                    text = "<option value='" + data[i]['id'] + "'>" + data[i]['title'] + "</option>"
                    // console.log(text)
                    $('#minutia').append(text)
                }
            }
        })
    }
