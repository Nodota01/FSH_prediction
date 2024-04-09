$(document).ready(function() {
    $("#submit-button").click(function(event) {
        if(!$("#prediction-form").valid()){
            return;
        }
        // 使用 serializeJSON 序列化表单数据为 JSON 对象
        var requestData = $("#prediction-form").serializeJSON();
        // 将 JSON 对象中的空值移除
        requestData = removeEmptyValues(requestData);
        // 调用接口
        $.ajax({
            type: "POST",
            url: "/api/single",
            contentType: "application/json",
            data: JSON.stringify(requestData),
            success: function(response) {
                $("#prediction-result").html(response.output);
            },
            error: function(xhr, status, error) {
                $("#prediction-result").html("Error: " + error);
            }
        });
    });

    $("#dual-submit-button").click(function(event) {
        if(!$("#dual-prediction-form").valid()){
            return;
        }        
        // 使用 serializeJSON 序列化表单数据为 JSON 对象
        var requestData = $("#dual-prediction-form").serializeJSON();
        // 将 JSON 对象中的空值移除
        requestData = removeEmptyValues(requestData);
        // 调用接口
        $.ajax({
            type: "POST",
            url: "/api/dual",
            contentType: "application/json",
            data: JSON.stringify(requestData),
            success: function(response) {
                $("#dual-egg").html(response.nor);
                $("#dual-fsh").html(response.fsh);
            },
            error: function(xhr, status, error) {
                $("#prediction-result").html("Error: " + error);
            }
        });
    });

    $("#s1s2-submit-button").click(function(event) {
        if(!$("#s1s2-prediction-form").valid()){
            return;
        }        
        // 使用 serializeJSON 序列化表单数据为 JSON 对象
        var requestData = $("#s1s2-prediction-form").serializeJSON();
        // 将 JSON 对象中的空值移除
        requestData = removeEmptyValues(requestData);
        // 调用接口
        $.ajax({
            type: "POST",
            url: "/api/s1s2",
            contentType: "application/json",
            data: JSON.stringify(requestData),
            success: function(response) {
                $("#s1s2_eggs_result").html(response.total_eggs);
                $("#s1s2_fsh_result").html(response.fsh);
            },
            error: function(xhr, status, error) {
                $("#prediction-result").html("Error: " + error);
            }
        });
    });

    // 监听身高和体重输入框的变化事件
    $("#height, #weight").on("input", function() {
        var height = parseFloat($("#height").val());
        var weight = parseFloat($("#weight").val());

        // 如果身高和体重都不为空，则计算 BMI
        if (!isNaN(height) && !isNaN(weight)) {
            var BMI = weight / ((height / 100) * (height / 100));
            $("#BMI").val(BMI.toFixed(2)); // 设置 BMI 输入框的值，保留两位小数
        } else {
            $("#BMI").val(""); // 如果身高或体重为空，则清空 BMI 输入框的值
        }
    });

    $("#bFSH, #bLH").on("input", function() {
        var bFSH = parseFloat($("#bFSH").val());
        var bLH = parseFloat($("#bLH").val());
        if (!isNaN(bFSH) && !isNaN(bLH)) {
            var FSH_LH = bFSH / bLH;
            $("#FSH_LH").val(FSH_LH.toFixed(2));
        } else {
            $("#FSH_LH").val("");
        }
    });

    // 监听身高和体重输入框的变化事件
    $("#height2, #weight2").on("input", function() {
        var height = parseFloat($("#height2").val());
        var weight = parseFloat($("#weight2").val());
        if (!isNaN(height) && !isNaN(weight)) {
            var BMI = weight / ((height / 100) * (height / 100));
            $("#BMI2").val(BMI.toFixed(2));
        } else {
            $("#BMI2").val("");
        }
    });
    $("#bFSH2, #bLH2").on("input", function() {
        var bFSH = parseFloat($("#bFSH2").val());
        var bLH = parseFloat($("#bLH2").val());
        if (!isNaN(bFSH) && !isNaN(bLH)) {
            var FSH_LH = bFSH / bLH;
            $("#FSH_LH2").val(FSH_LH.toFixed(2));
        } else {
            $("#FSH_LH2").val("");
        }
    });

    // 监听身高和体重输入框的变化事件
    $("#height3, #weight3").on("input", function() {
        var height = parseFloat($("#height3").val());
        var weight = parseFloat($("#weight3").val());
        if (!isNaN(height) && !isNaN(weight)) {
            var BMI = weight / ((height / 100) * (height / 100));
            $("#BMI3").val(BMI.toFixed(2));
        } else {
            $("#BMI3").val("");
        }
    });
    $("#bFSH3, #bLH3").on("input", function() {
        var bFSH = parseFloat($("#bFSH3").val());
        var bLH = parseFloat($("#bLH3").val());
        if (!isNaN(bFSH) && !isNaN(bLH)) {
            var FSH_LH = bFSH / bLH;
            $("#FSH_LH3").val(FSH_LH.toFixed(2));
        } else {
            $("#FSH_LH3").val("");
        }
    });
});

// 移除 JSON 对象中的空值
function removeEmptyValues(obj) {
    Object.keys(obj).forEach(function(key) {
        if (obj[key] == 0) {
            delete obj[key];
        }
    });
    return obj;
}
