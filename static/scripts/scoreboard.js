var s =0;
var w=0;
function incrementScore() {
    document.getElementById("runs").innerHTML = ++s;
  }

function decrementScore() {
    if (s>0)
    {
    document.getElementById("runs").innerHTML = --s;
    }
 }

 function incrementWicket() {
    document.getElementById("wickets").innerHTML = ++w;
  }

  function decrementWicket() {
    if (w>0)
    {
    document.getElementById("wickets").innerHTML = --w;
    }
 }

 function battingTeam() {
        var name=document.getElementById("battingTeam").value;
        document.getElementById("currentTeam").innerHTML = name;
  }

  function bat1() {
    var name=document.getElementById("bat1").value;
    document.getElementById("batsman1").innerHTML = name;
}

function bat2() {
    var name=document.getElementById("bat2").value;
    document.getElementById("batsman2").innerHTML = name;
}

var b1S=0,b1B=0,b2S=0,b2B=0,ovr=0;

function incrementB1Score() {
    document.getElementById("b1score").innerHTML = ++b1S;
  }

function incrementB2Score() {
document.getElementById("b2score").innerHTML = ++b2S;
}

function incrementB1Balls() {
    document.getElementById("b1balls").innerHTML = ++b1B;
    }

function incrementB2Balls() {
    document.getElementById("b2balls").innerHTML = ++b2B;
    }

    
function incrementOvers() {
    document.getElementById("overs").innerHTML = ++ovr;
    }