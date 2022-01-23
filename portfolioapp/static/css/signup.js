function matchpass(){
    var firstpassword=document.getElementById("psw").value;
    var secondpassword=document.getElementById("psw-repeat").value;
        if(firstpassword==secondpassword){
        return true;
        }
        else{
        alert("password must be same!");
        return false;
        }
        }