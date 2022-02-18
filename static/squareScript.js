function squareRoot() {
    var numberInput = document.getElementById("sqrtNumber").value;

    var url = "/squareRoot";

    axios({
        method: "post",
        url: url,
        data: {
            number: numberInput,
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