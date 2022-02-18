function convert() {
    var scoreInput = document.getElementById("scoreNum").value;

    var url = "/scoreConv";

    axios({
        method: "post",
        url: url,
        data: {
            score: scoreInput,
        },
        headers: {
            "Content-Type": "application/json"
        }
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    )
}