$.ajax({
    url: "/data_cook",
    type: "POST",
    contentType: "application/json;charset=UTF-8",
    dataType: "json",
    data: JSON.stringify({cook_id: thisid}),
    success: function(response) {
        console.log(response);
    },
});