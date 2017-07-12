"use strict";

const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://10.215.56.158')

const mraa = require('mraa'); //require mraa
console.log('MRAA Version: ' + mraa.getVersion());

let pinup = new mraa.Gpio(46); //setup digital read on pin 47
let pindown = new mraa.Gpio(31); //setup digital read on pin 44
let pinleft = new mraa.Gpio(15); //setup digital read on pin 165
let pinright = new mraa.Gpio(45); //setup digital read on pin 45
let select = new mraa.Gpio(33); //setup digital read on pin 48
let pina = new mraa.Gpio(47); //setup digital read on pin 49
let pinb = new mraa.Gpio(32); //setup digital read on pin 46

pinup.dir(mraa.DIR_IN);
pindown.dir(mraa.DIR_IN);
pinleft.dir(mraa.DIR_IN);
pinright.dir(mraa.DIR_IN);
select.dir(mraa.DIR_IN);
pina.dir(mraa.DIR_IN);
pinb.dir(mraa.DIR_IN);

var state = 'closed'

client.on('connect', function () {   
 client.publish('lupe/connected', 'true')
  sendStateUpdate()
})


function sendStateUpdate () {  
  console.log('Sending state %s', state)
  client.publish('lupe/state', 'true')
}


function handleAppExit (options, err) {
  if (err) {
    console.log(err.stack)
  }

  if (options.cleanup) {
    client.publish('lupe/connected', 'false')
  }

  if (options.exit) {
    process.exit()
  }
}

process.on('exit', handleAppExit.bind(null, {  
  cleanup: true
}))
process.on('SIGINT', handleAppExit.bind(null, {  
  exit: true
}))
process.on('uncaughtException', handleAppExit.bind(null, {  
  exit: true
}))

function periodicActivity() {
   if(pinup.read()==0){
    client.publish('lupe/moveforward','true');
    console.log("Message is published");    

   }else if(pindown.read()==0){
    client.publish('lupe/movebackward','true');
    console.log("Message is published");    

   }else if(pinleft.read()==0){
    client.publish('lupe/moveleft','true');
    console.log("Message is published");    

   }else if(pinright.read()==0){
    client.publish('lupe/moveright','true');
    console.log("Message is published");    

   }else if(select.read()==0){
    client.publish('lupe/movestop','true');
    console.log("Message is published");    

   }else if(pina.read()==0){
    client.publish('lupe/moveleft','true');
    console.log("Message is published");    

   }else if(pinb.read()==0){
    client.publish('lupe/moveright','true');
    console.log("Message is published");    

   }
//client.end();
}

setInterval(periodicActivity, 500);



