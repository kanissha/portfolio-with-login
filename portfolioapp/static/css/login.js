function validate()
{
    var usr=document.getElementById("username").value;
    var pass=document.getElementById("password").value;

    if(usr=="Harishini" && pass=="Hari*123")
    {
        alert("Login successful");
        return true;
    }
    else{
       
        alert("Invalid Username/Password combination,");
        return false;
    }
}