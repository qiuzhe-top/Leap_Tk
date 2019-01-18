$('#excel-file').change(function (e) {
    var files = e.target.files;

    var fileReader = new FileReader();
    fileReader.onload = function (ev) {
        try {
            var data = ev.target.result,
                workbook = XLSX.read(data, {
                    type: 'binary'
                }), // 以二进制流方式读取得到整份excel表格对象
                persons = []; // 存储获取到的数据
        } catch (e) {
            console.log('文件类型不正确');
            return;
        }

        // 表格的表格范围，可用于判断表头是否数量是否正确
        var fromTo = '';
        // 遍历每张表读取
        for (var sheet in workbook.Sheets) {
            if (workbook.Sheets.hasOwnProperty(sheet)) {
                fromTo = workbook.Sheets[sheet]['!ref'];
                // console.log(fromTo);
                persons = persons.concat(XLSX.utils.sheet_to_json(workbook.Sheets[sheet]));
                // break; // 如果只取第一张表，就取消注释这行
            }
        }
        var last = JSON.stringify(persons);
        console.log(last)
        $.ajax({
            url: '/ajax_Tk_add_all',
            type: 'POST',
            data: {
                data:last
            },
            success: function (arg) {
                // data = JSON.parse(arg.msg);
                // console.log(data);
                // for (i in data) {
                //     text = "<tr>" + "<th>" + i + "</th>" + "<th>" + data[i] + "</th>" + "</tr>"
                //     $('.get_back').append(text)
                // }
            }
        })
        // 清空表格
        $(".tablehead").html("");
        $(".tablebody").html("");
        for (var j = 0; j < persons.length; j++) {
            var arr = persons[j];
            if (j == 0) {
                $(".tablehead").append("<tr class='exceltitle'></tr>");
            }
            $(".tablebody").append("<tr class='excelcontent'></tr>");
            for (var i in arr) {
                //alert(i+"---"+arr[i]);
                if (j == 0) {
                    $(".exceltitle").append("<th>" + i + "</th>");
                }
                $(".excelcontent").eq(j).append("<td>" + arr[i] + "</td>");
            }
        }

    };
    // 以二进制方式打开文件
    fileReader.readAsBinaryString(files[0]);
});
//excel批量导入 end