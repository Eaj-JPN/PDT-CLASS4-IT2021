function hypotenuse() {
    var baseNum = document.getElementById("num1").value;
    var altNum = document.getElementById("num2").value;

    var url = "/hypo";

    axios({
        method: "post",
        url: url,
        data: {
            base: baseNum,
            altitude: altNum,
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