## **6.1: DC Motor og Transistors**
### **Liður 1:**

   1. **Hvernig er skrefmótor (e. stepper motor) ólíkur hefðbundnum DC mótor?**
      * **Svar:**  Skréfmótor er hægt að stjórna með miklu nákvæmnari hætti vegna þess að hann þarf microcontroller til þess að virka, skrefmótorar snúast þó miklu hægar(bara 200-2000 Rpm) og eru með hægari viðbrags tíma. Skrefmótor inniheldur ekki bursta (brushless) og er í opnri hringrás(open loop)

   1. **Hvernig er stýrimótor (e. servo motor) ólíkur hefðbundnum DC mótor?**
      * **Svar:** Servo Motor er einfaldlega DC Motor sem ekki er hægt að keyra stansluast. Hann er miklu nákvæmari en getur bara snúið í hálfhring (180°). Servo mótor er samsettur af fjórum hlutum: DC mótor, gírabox, stjórnrás og stöðu skynjara.
   1. **Hvernig er hægt að stjórna í hvora áttina DC mótor snýst?**
      * **Svar:**  Með því að svissa snúrunum sem eru tengd í + og - rafskautin. Þá verða rafskautin öfug og mótorinn byrjar að snúast í hina áttina.  
   1. **Hvað gerir transistor?**
      * **Svar:**  Transistor er hálfleiðari sem er notaður til þess að magna upp rafmagn eða skipta um rafræn merki(on/off 0/1). Hann er samsettur úr hálfleiðandi efni og er yfirlett með að minnsta kosti þjrú rafskaut til að tengjast ytri rafrásinni.
   1. **Hver er munurinn á NPN og PNP transistorum?**
      * **Svar:**  NPN Tranistor stendur fyrir Negative-Positive-Negative Transistor og PNP stendur fyrir Positive-Negative-Positive Tranistor. NPN Tranistor hleypur rafmagni í gegn þegar að hann fær í rafmagn í base pinnann. PNP Tranistor stoppar rafflæðið ef að hann fær í rafmagn base pinnann.

### **Liður 2:**
  * [Linkur að tinkercad DC mótor verkefni]( https://www.tinkercad.com/things/4ZrOxAIUbhs )
### **Liður 3:**
   1. **Afhverju þurfum við að nota PWM pinna til að stýra DC mótor?**
      * **Svar:** Pwm signal sendir röð af on eða off merkjum. On væri þá t.d. 5 volt og off væri 0 volt. Ef að on og off merkin er á jafn lengi (%50 hvor) þá myndi Dc mótorinn fá helmingi minni spennu eða 2.5 volt frá brettinu í stað 5 volta og þar af leiðandi myndi hann hægja á sér.
   2. **Afhverju þurfum við að nota viðnám, transistor og diode með DC mótor í _Lesson 13. DC Motors_?**
        * **Svar:** Ef að ég myndi tengja DC Mótorinn beint í Arduino brettið þá ég hættu á því að skemma það. Arduino brettið getur sjálft ekki veitt aflið sem að DC mótorinn þarf beint. Transistorinn er notaður sem rofi sem að notar lítð rafmagn frá brettinu og notar það til þess að stjórna mikið stærri orkuna í mótornum. Viðnámið er tengt í transistorinn til þess að minnka aflið sem að fer beint í transistorinn. Díóðan leyfir rafmagninu bara að flæða í eina átt. Þegar þú slekkur á vélinni færðu neikvæða spennu sem getur skemmt Arduino eða tranistorinn. Díóðan verndar gegn þessu með því að skammhlaupa afturstrauminn frá mótornum.
### **Liður 4:**
  * [Linkur að Verklegu DC mótor](https://youtu.be/ptcVm60CB2Y)
    
## 6.2: Servo Motors (5%)


1. Fylgdu [Lesson 14. Servo Motors](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors) og settu hann upp í:

   1. TinkerCad.
       * [Sweep](https://www.tinkercad.com/things/bnDQIUGGr5V)
       * [Knob](https://www.tinkercad.com/things/iTC7dDrUpBj)
   2. Verklega
       * [Sweep](https://youtu.be/0Tjf8Tb719g)
       * [Knob](https://youtu.be/cTX8Qx7M318)
   
2. Svaraðu eftirfarandi spurningum:

   1. Afhverju er heppilegt að nota rafþéttir með servo motor?
    * **Svar:** Servo mótor dregur töluvert af krafti þegar hann er að ræsa sér. Þessi skyndilega mikla eftirspurn af rafmagni  getur verið nóg til að lækka spennuna á Arduino brettinu, svo að hann endurstillir sig. Þá er gott að setja rafþétti á mill 5v og GND á brauðbrettinu. Rafþéttirinn geymir ís sér rafmagn sem að servo mótorinn getur svo notað þegar hann er að ræsa sér. 
   2. Hver er munurinn á batterí og rafþéttir (capacitor)?
    * **Svar:** Rafhlaða geymir raforku í formi efnaorku (Lithium eða Alkaline til dæmis) en rafþéttir geymir raforku á segulsviði. Þess vegna geyma rafhlöður mikið af hleðslu en þær hlaðast og afhlaðast mjög hægt. Gott er að nota rafþétti í rafrás þegar að einhver hlutur krefst skyndilega mikillar orku.
3. Nefndu dæmi um i hvaða tilfellum eftirfarandi mótorgerðir væru notaðar: 
    1. Hefðbundinn DC mótor.
       * **Svar:** DC mótorar eru notaðir í barna leikföngum, hlaupabrettum, drónum, færiböndum o.s.frv.
    2. Skrefmótor.
       * **Svar:** Skrefmótorar er víða notaðir í 3d prenturum, logsuðun, nútíma prentvélum, borvélum o.s.frv. 
    3. Stýrimótor.
          * **Svar:** Stýrimótorar eru notaðir í autofocus á myndavélum, til þess að stýra útlimum í vélmennum, staðsetningu á loftneti, sjálfvirkum hurðum o.s.frv.
4. Hvað snýst servo motor margar gráður þegar hár púls (e. pulse) varir í 1.5 millisekúndur?
    * **Svar:** Mótrinn myndi snúast 90 gráður.
 