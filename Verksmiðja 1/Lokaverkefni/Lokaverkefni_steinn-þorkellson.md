## Lokaverkefni
1. Skoðaðu [Vélbúnaður og blink: Ladyada´s lesson 0, 1 og 2](https://learn.adafruit.com/series/ladyadas-learn-arduino) og svaraðu eftirfarandi spurningum:

   1. Hvað er þetta á Arduino og hlutverk þess (sjá mynd)?
![ARduino Uno]
      * Þetta er aflgjafi. Aflgjafinn getur tekið á móti 7-20 voltum og lækkar það niður í 5 volt svo að brettið eyðilegst ekki
   1. Að hvaða leyti er gagnapinni 13 sérstakur í Arduino Uno?
      * Gagnapinni 13 er líka tengdur við L LED, þegar pinni 13 fær signal þá mun L LED blikka.
   2. Hver er munurinn á digtial og analog input pinnum?
      * Digital input pinnar nota 5 volt sem high signal og 0 volt sem low signal (on/off 0/1). Analog input pinnar geta tekið á mót öllu frá 0-5 volts.
   3. Hjá sumum digital pinnum er tilda merki (~) fyrir PWM. Hvað er e. Pulse Width Modulation (PWM) og fyrir hvað er það notað?
        * Pwm er signal sem sendir röð af on eða off bylgjum (square wave). On væri þá t.d. 5 volt og off væri 0 volt. Ef að on og off merkin er á jafn lengi (%50 hvor) þá myndi Dc mótorinn fá helmingi minni spennu eða 2.5 volt frá brettinu í stað 5 volta og þar af leiðandi myndi hann hægja á sér.

1. Pushbutton (Digital Input) 
    * [Tinkercad linkur]( https://www.tinkercad.com/things/a0n9ko1Z7S2)
    * [Tinkercad Upptaka 1](https://youtu.be/NyX2I4OZjck)
    * [Verklegt](https://youtu.be/fBRNeDER414)
    * [Tinkercad Upptaka 2](https://youtu.be/2zA26ELIU2U)
    * [Verklegt 2](https://youtu.be/RZcvrq24P3o)
   1. _Hverju myndi það breyta ef við myndum tengja viðnám fyrir hnappinn í 5V í staðinn fyrir jörð (GND)?_
      * Þá er ljósið stöðugt kveikt og hnappurinn hættir að virka
   2. _Afhverju þarf pinni 2 að vera tengdur við jörð?_
      * Svo að hringrásin lokist. 
   3. _Breyttu kóðanum þannig að með að ýta á takkann þá ser slökkt á LED ljósi sem myndi annars lýsa stöðugt._
      *  if (buttonState == HIGH) {
          digitalWrite(13, LOW);
        } else {
          digitalWrite(13, HIGH);
        }

2. Potentiometer (Analog Input)
    * [Tinkercad Linkur]( https://www.tinkercad.com/things/0V3aOtxD48n )
    * [Tinkercad Upptaka](https://youtu.be/cnV2iR4Yutg)
    * [Verklegt](https://youtu.be/pcieTwEIRoM)
   1. _Arduino er með 10 bita analog to digital converter (ADC). Hvernig virkar ADC og hvaða gildi er verið að vinna með?_
        * ADC breytir spennu (analog) yfir í stafræna tölu. 10 bit ADC í arduino getur skynjað 1024 einstök analog signal.
   2. _Hvað gerist ef við tengjum digital skynjara við analog pinna?_
      *    Ljósið hættir að blikka en virkar ennþá.

3. Using the Serial Monitor í 
    * [Tinkercad verkefni](https://www.tinkercad.com/things/740n5No6evM)
    * [Tinkercad upptaka](https://youtu.be/125Y6-6V3Dg)
   * Fékk 1 til að virka, en þegar ég ýti á takkan þá aftengist ardino tölvunni. 2 virkaði í smástund en sýndi bara hexadecimal tölur.
   1. _Hvað þýðir 9600 baud í Serial.begin(9600) og hvað gerist ef þú breytir gildinu?_
      * 9600 í serial.begin(9600) þýpir að arduino sendir 9600 bits á sekúndu af binary 1 og 0 tölum í serial monitor. Ef gild' er lækkað þá hægist á serial monitor og það tekur lengri tíma að sjá breytingarnar. Öfugt gerist ef gildið er hækkað.
4. Photoresistor (Analog Input) í 
   * [Tinkercad Linkur](https://www.tinkercad.com/things/jKanbNQFocl)
    * [Tinkercad Upptaka](https://youtu.be/huZMxvmxU6I)
    * [Verklegt](https://youtu.be/EP05DoQMGQ0)
   1. _Útskýrðu færibreyturnar og gildin í map fallinu. Afhverju þarf úttakið í analogWrite að vera á bilinu 0-255?_
       * Map breytir t.d. 10bit(1024) tölur niður í 8bit(256) tölur.Map tekur inn 4 gildi fyrstu tvo gildin eru tölurnar sem þú vilt breyta úr og seinni tvær eru þær sem þú vilt breyta í. Úttakið í analogwrit þarf að að vera 0-255 svo að digital pinnin sem fer í led peruna geti gert sitt gagn út af því að hann virkar bara með 8bit gildi (0-255).
       <br>
       `analogWrite(9, map(sensorValue, 0, 1023, 0, 255));`

5. Ultrasonic Distance Sensor 
    * [Tinkercad Linkur](https://www.tinkercad.com/things/bTA6zORvgkV)
    * Tinkercad bilaði hjá mér, hver sekúnda er mínúta að líða í simulator, finn enga lausn eins og er, ætla að reyna aftur seinna.
    * [Verklegt](https://youtu.be/stHmNkFrLrY)
    1. _Breyttu kóðanum þannig að hann vinnur eingöngu með sentimetra._
       * Eyða þessum línum: `int inches = 0;` | `Serial.print(inches); Serial.println("in");`
    2. _Hvað gerir timeout í eftirfarandi falli? `pulseIn(pin, value, timeout);`_
         * Timeout er tíminn í míkrósekúndum sem það á bíða eftir að fá pulse signal. Ef ekkert signal er innan við t.d. 1000 míkrósekúndum þá skila hann frá sér 0 gildi.

6.  Project 6: Light Theremin (hátalari og ljósviðnám) í 
    * [Tinkercad Linkur](https://www.tinkercad.com/things/jtZfKMLZYFe)
    * Ákvað að sleppa tinkercad upptökunni vegna þess að hljóðið er óbærilegt og það er svo hægt hjá mér.
    * [Verklegt](https://youtu.be/miHRmUZRipg)
    1. _Hvað er verkhlutfall (e. duty cycle) og hvernig tengist það tíðni (e. frequency)?_
       * Duty cycle er prósentan af því sem að signal er virkt eins og t.d. 50%. Frequency er hversu oft signalið er virkt á sekúndi(hversu mörg duty cycle á sekúndu). Tökum dæmi: ef duty cycle er 50% og tíðnin er 500 hertz, þá myndi signalið vera virkt 5 sinnum á 10 millisekúndum. Ef að duty cycle er 50% og tíðnin er 1000 hertz, þá myndi signalið vera virkt 10 sinnum á 10 millisekúndum.
    2. _Tíðni (e. frequnzy) er mæld í Hertz (Hz). Útskýrðu hvernig það er gert._
       * Tíðni er mæld með því að gá hversu margar bylgjur(duty cycle) fara framhjá á sekúndu. Til dæmis er tíðnin á nótunni A 440Hz, ef þú spilar A á gítar þá titrar strengurinn á 440hz á sekúndu.