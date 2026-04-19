SPRINT 4 - Jan Ruz - CRUD amb FastAPI i MongoDB (Frontend, Backend)

Secció de commits:

Commit 05/04/2026
Commit 13/04/2026
Commit 14/04/2026 
Commit 15/04/2026

En aquesta pràctica aprenem l'ús sincronitzat de FastAPI per al desenvolupament del backend i de les API amb Python i MongoDB per a l'allotjament i la creació d'una base de dades on realitzar una sèrie de proves CRUD per sostreure, afegir, modificar o esborrar dades/entrades, tot això sabent el flux de funcionament de dades entre el Backend, Frontend i la pròpia. Tindrem una carpeta per a tots dos apartats i una altra per a les proves. Cal ressaltar que dins dels temes escollits s'ha escollit el Gestor de Pel·lícules.

Backend (backend/)
Aquesta carpeta conté tota la lògica del servidor i la connexió a la base de dades.

<img width="758" height="68" alt="image" src="https://github.com/user-attachments/assets/4c0b0f84-e618-48c3-b24f-2cc240f38ca6" />

Primer tenim app.py, que es relaciona com el cervell de l'aplicació. Està desenvolupat amb FastAPI i estableix la connexió asíncrona amb la base de dades MongoDB utilitzant PyMongo Async. Defineix l'estructura de les dades (els models) mitjançant Pydantic, aplicant validacions estrictes per garantir que la informació sigui correcta (Exemple: Que la puntuació de la pel·lícula estigui entre 1 i 5). A més d'això, exposa tots els endpoints que permetin realitzar les operacions CRUD i filtrar-ne el contingut, recalcar que també configura el CORS (Cross-Origin Resource Sharing) per permetre que la nostra pàgina web pugui intercanviar dades amb l'API de forma segura (és un punt opcional encara que arriba a ser obligatori perquè el backend no tingui problemes per connectar-se amb el frontend.

<img width="534" height="279" alt="image" src="https://github.com/user-attachments/assets/a752ff3d-7712-4e10-85fa-74a0a84aebec" />

<img width="752" height="277" alt="image" src="https://github.com/user-attachments/assets/ff59b3d1-56f1-4e2e-97cc-8aa2687db3c0" />

<img width="741" height="384" alt="image" src="https://github.com/user-attachments/assets/5586132a-537b-40db-a72c-f9209c56b0a0" />

D'altra banda tenim requirements.txt que llista de totes les dependències i llibreries de Python necessàries per aixecar l'entorn (FastAPI, Uvicorn, PyMongo, etc.). A part del propi FastAPI, afegim Uvicorn per emular una mena de servidor per funcionar, pyMongo que és com un controlador per a la connexió de MongoDB amb les apps fetes a Python, pydantic per validar dades i estructurar dades com a classes (class) (en aquest cas el [email] és per validar correus el utilitzar eines modernes sense haver dactualitzar la versió de Python.

<img width="171" height="120" alt="image" src="https://github.com/user-attachments/assets/3a4824af-ff87-433d-bada-5a92965598d5" />

Frontend (frontend/)
Aquesta carpeta conté els fitxers que conformen la pàgina web amb la qual l'usuari interactua. És la que es veu al capdavall, contrari al backend que per dir-ho així funciona per darrere.

<img width="762" height="62" alt="image" src="https://github.com/user-attachments/assets/cfba2ef2-3a91-49e1-8a29-b5053798b40a" />

Primer tenim l'index.html que és l'esquelet visual de la web. Conté tota l'estructura de la interfície: el formulari d'entrada de dades, els cercadors (per ID i per gènere) i la taula principal, també aplica les classes del framework CSS Skeleton per aconseguir un disseny més net. És el fitxer del text visual.

<img width="748" height="384" alt="image" src="https://github.com/user-attachments/assets/1f74f0c4-b5a2-4102-a519-b6a93aaa67db" />

Després styles.css és el dels estils i colors. S'encarrega dels retocs visuals personalitzats que el framework Skeleton no cobreix, com els marges personalitzats de la pàgina, la lletra petita per a les descripcions o el color vermell d'alerta per al botó d'eliminar.

<img width="448" height="262" alt="image" src="https://github.com/user-attachments/assets/95669781-202e-41b8-9bab-695aab7f5f41" />

Finalment javascript.js és l'arxiu que dóna vida a la pàgina web i la fa interactiva, això és perquè actua de pont entre el navegador de l'usuari i l'app.py ja que utilitza peticions asíncrones amb fetch per enviar i rebre dades de l'API en format JSON.

<img width="753" height="330" alt="image" src="https://github.com/user-attachments/assets/cbc077af-e1e7-443d-84b9-076f3cf585aa" />

Postman (tests/)
Aquesta carpeta bàsicament representa les proves un cop tot el desenvolupament està fet per veure si funciona mitjançant CRUD, el qual en aquest cas es desa en format JSON.

<img width="755" height="62" alt="image" src="https://github.com/user-attachments/assets/14869256-e1db-4ae9-8e1f-4afca956f192" />

<img width="750" height="278" alt="image" src="https://github.com/user-attachments/assets/d119efa3-99e8-4092-bb8a-36a3ecd92ca7" />

Tutorial de ejecución:

Abans de res clonar el repositori per utilitzar-lo en següents passos:

<img width="759" height="74" alt="image" src="https://github.com/user-attachments/assets/42dcfdbc-d1c7-4a62-bd72-c80eb7f4c414" />

El primer per passar al tutorial és que haurem de veure si tenim Python instal·lat i quina versió. Un cop comprovat que està instal·lat podem (recomanable) crear un entorn virtual per no tenir conflictes de dependències, per això tenint Python instal·lat posem la següent ordre i l'activem posteriorment amb python3 -m venv (RESALTAR QUE LES DUES PRIMERES CAPTURES SÓN D'EXEMPLE D'UN ALTRE TREBALL):

<img width="600" height="38" alt="image" src="https://github.com/user-attachments/assets/564d6e14-169a-42a0-8b45-23576a1b3b71" />

<img width="602" height="73" alt="image" src="https://github.com/user-attachments/assets/c08acf65-053d-407b-b464-53d717490b5f" />

<img width="766" height="52" alt="image" src="https://github.com/user-attachments/assets/a9c560c7-e29c-4b62-b363-1a4526a02b15" />

<img width="755" height="127" alt="image" src="https://github.com/user-attachments/assets/6568253e-4369-44af-bdb1-88bbeb97fa42" />

Un cop fet això tenim assegurat un espai per poder desenvolupar sense problemes, i haurem de passar a la instal·lació de les llibreries esmentades anteriorment a l'apartat del Backend a requirements.txt, per això haurem de fer la següent ordre:

<img width="304" height="29" alt="image" src="https://github.com/user-attachments/assets/9f05bd5b-d866-4789-86c9-bdbe31c6ca95" />

A través d'això es començaran a instal·lar aquestes llibreries, encara que de tant en tant cal anar amb compte perquè hi ha conflictes amb la URL de MongoDB en aquest cas si no està ben posada o, també en aquest cas, per no tenir informació sensible com la cadena de connexió ficada a l'arxiu, podem exportar l'URL per a més seguretat sense afegir dades (això sí, és més molest ja que s'ha de fer cada cop):

<img width="757" height="62" alt="image" src="https://github.com/user-attachments/assets/062b45d6-99ff-456e-bbd9-5b46d90d4c3a" />

Un cop fet això mirarem d'executar Uvicorn amb el fitxer .py per veure el Swagger:

<img width="757" height="289" alt="image" src="https://github.com/user-attachments/assets/d6ab2aff-db3c-4d90-a665-b0b1ff92efa6" />

<img width="1162" height="706" alt="image" src="https://github.com/user-attachments/assets/1fd8e92c-9b88-4d14-a85a-8daee66ddc13" />

A la pàgina ens sortirà les diferents modalitats del CRUD inclòs un GET per ID, el qual sortirà un menú desplegable amb l'opció d'executar una de les modalitats:

<img width="1162" height="706" alt="image" src="https://github.com/user-attachments/assets/9b4c2fc5-1d09-4e02-a5a9-19856df79eb9" />

<img width="1024" height="541" alt="image" src="https://github.com/user-attachments/assets/a0e975b4-fa0e-4f2c-8a34-2b6711603830" />

<img width="1043" height="266" alt="image" src="https://github.com/user-attachments/assets/98fc1c95-8064-43b6-ae0a-13121b82c3f2" />

<img width="1020" height="369" alt="image" src="https://github.com/user-attachments/assets/bdd37ba5-7a31-4b96-a248-f7aa6576c217" />

<img width="1028" height="257" alt="image" src="https://github.com/user-attachments/assets/81b9501b-beaf-499c-8679-41326c438d50" />

Una altra forma d'executar les funcionalitats del CRUD és fer-ho des del nostre propi frontend a través del fitxer HTML creat anteriorment, el quin es pot gestionar usant el fitxer index.html (obrint-lo):

<img width="103" height="76" alt="image" src="https://github.com/user-attachments/assets/4c7a294a-1625-4515-8c3a-df7aa5ed1594" />

<img width="1101" height="544" alt="image" src="https://github.com/user-attachments/assets/cddabd68-bb87-4ef1-927f-498d67c575cc" />

<img width="1061" height="299" alt="image" src="https://github.com/user-attachments/assets/5352296b-fc81-4bb6-96f8-41c8f65b59b6" />

Aquesta forma és força intuïtiva també, amb un menú per poder incloure els mateixos paràmetres d'una pel·lícula (puntuació, nom, descripció, etc.). A més d'això, també tenim un altre apartat per cercar una pel·lícula pel vostre ID per veure el seu estat. Un cop completat podem afegir-lo a la llista a "Afegir a la llista", i a sota ens apareixerà cada pel·lícula que s'afegeixi:

<img width="1101" height="545" alt="image" src="https://github.com/user-attachments/assets/84cb5334-f2fd-4522-a804-7b517b1c8659" />

<img width="1071" height="370" alt="image" src="https://github.com/user-attachments/assets/f1642880-bf6e-4746-94d7-3899a31a3329" />

En voler comprovar la seva existència a la base de dades, podem anar a MongoDB Atlas i comprovar-ho:

<img width="1137" height="401" alt="image" src="https://github.com/user-attachments/assets/fb2999ed-f23e-4989-be07-541279ef323f" />

D'altra banda en l'àmbit de proves a part del Swagger, una manera més ordenada és fer-la des de Postman, el qual el JSON de la carpeta /tests/ és una exportació de la col·lecció creada + CRUD:

<img width="278" height="181" alt="image" src="https://github.com/user-attachments/assets/8dc56126-12bb-4bc5-8ccb-b7008eb93581" />

<img width="846" height="240" alt="image" src="https://github.com/user-attachments/assets/5b88ce1a-1757-42ea-8c68-9600b890d73d" />

<img width="1033" height="296" alt="image" src="https://github.com/user-attachments/assets/a872bc4c-ec4e-47b2-891f-e9b26a94176e" />

<img width="776" height="197" alt="image" src="https://github.com/user-attachments/assets/3ab0f42e-eafd-49f2-a88e-c67763cd4f95" />

<img width="739" height="186" alt="image" src="https://github.com/user-attachments/assets/f7934b18-b4be-4ec1-b40b-0ea280bfc44b" />

<img width="804" height="198" alt="image" src="https://github.com/user-attachments/assets/19c40ff6-5a95-4e71-a805-42b329a751a6" />

Per fer funcionar aquestes proves, cal importar el .JSON a Postman i executar "Run Collection".

<img width="384" height="50" alt="image" src="https://github.com/user-attachments/assets/e8b4836e-3561-4525-b047-6d76027c0c13" />
<img width="452" height="185" alt="image" src="https://github.com/user-attachments/assets/eb7b8853-a82e-46c6-b723-5488429826a1" />

Videotutorial per al Frontend (1) i Postman (2):
https://drive.google.com/file/d/1nL92Uma5y9DxEUYi7vCusGbQXwbjPLxN/view?usp=sharing
https://drive.google.com/file/d/1iovQrOeBO3_ZKfEeX2jw7fO57dXi-i0V/view?usp=sharing
