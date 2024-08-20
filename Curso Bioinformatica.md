# HERRAMIENTAS BIOINFORMÁTICAS
Profesor: Jose Luis Sánchez

# Sección 1: INTRODUCCIÓN. BASES DE DATOS BILOÓGICAS
1953 James Watson y Francis Crick descubrieron estructura ADN
Rosalind Franklin fotografía 51, a partir de la cual los dos anteriores descubrieron la molécula de ADN.

2003 Secuencia completa del ADN Humano. Comenzó en 1990. 3000 millones de dolares.

Secuencia de nucleótidos de adn tenemos mucha información.

## 2. ¿Qué son las bases de datos biológicas?
Secuencias de aminoácidos, o de nucleótidos, secuencias completas, enfermedades, anotaciones,

Ejemplos: GenBank y WGS bbdd de secuencias genéticas pertenecientes a NCBI. Son gratuitas.

## 3. Tipos de bases de datos biológicas

Podemos clasificar las bases de datos biológicas siguiendo múltiples criterios. Una forma de clasificación comúnmente utilizada en bioinformática es la que se muestra a continuación:


**BASES DE DATOS PRIMARIAS**
Contienen archivos de datos en “crudo”, sin filtrar, enviados por multitud de laboratorios. Estos datos no son revisados por el personal de las bases de datos, pero deben de cumplir unos requisitos concretos y estar debidamente anotados por el remitente (por ejemplo, se debe especificar el organismo al que pertenecen o el intervalo de la región codificante si se tratase de la secuencia de un gen, etc). Algunos ejemplos son:

- GenBank: Pertenece al NCBI.

- ENA: (European Nucleotide Archive). Pertenece al EMBL-EBI.

- DDBJ: (Banco de Datos de ADN de Japón). Pertenece al NIG


Todas ellas contienen secuencias de nucleótidos (ADN genómico y ARN).

Son de libre acceso a través de internet.

Intercambian sus datos cada 24 horas (pertenecen al International Nucleotide Sequence Database Collaboration).

Aunque contengan los mismos datos, cada DB (Data Base) tiene su propio formato para representarlos.

Son redundantes. Pueden contener varios registros para cada secuencia, ya que cada laboratorio puede enviar el suyo propio.



- PDB: (Protein Data Bank). Estructura tridimensional de proteínas.



**BASES DE DATOS SECUNDARIAS**
Contienen datos ya procesados informáticamente o curados (revisados manualmente por el personal experto de la base de datos). Los datos provienen de las BBDD primarias. Algunos ejemplos son:

- RefSeq:  ADN, ARN y proteínas. Depende del NCBI. Contiene un único registro para cada molécula biológica. Ofrece mucha información y muy fiable.

- UNIPROTKB:  Secuencias de proteínas con muchas anotaciones y también muy fiable. Depende de UNIPROT y unifica la información de dos bases de datos:
 TrEMBL: Traducción automática de EMBL.

 SWISS-PROT:  Proteínas anotadas por expertos.



**BASES DE DATOS ESPECIALIZADAS**
Están especializadas en un tema muy concreto de investigación. A continuación se muestran algunos ejemplos.

- PubMed: Base de datos de citas y resúmenes de literatura biomédica y revistas adicionales de ciencias de la vida. Pertenece al NCBI.

- OMIM: (Online Mendelian Inheritance in Man): Base de datos de genes humanos y transtornos genéticos. Pertenece al NCBI.

- TAIR:  Base de datos de biología genética y molecular para la planta Arabidopsis thaliana.


Entra en los enlaces anteriores para ir familiarizándote con las diferentes páginas web de estas bases de datos.


#### NOTA TEÓRICA: Transcripción del adn al arn
Células procariotas: material genético sin núcleo.
Célutas eucariotas: material genético dentro del núcleo.

La síntesis de proteínas es un proceso por el cual las células producen nuevas proteínas. Se realiza en dos pasos: primero, el ADN se convierte en ARN mensajero (transcripción), y luego ese ARN mensajero dirige la construcción de la proteína (traducción).
Como resultado de la transcripción, la mayoría de los genes se convierten en ARNm. Sin embargo, algunos genes se transcriben en otros tipos de ARN, como el ARN ribosomal (ARNr) y el ARN de transferencia (ARNt), que también son importantes para la síntesis de proteínas. La importancia de estos dos tipos de ARN en el proceso es igual a la del ARNm.
La síntesis de proteínas se realiza en los Ribosomas




https://www.youtube.com/watch?v=E_ImINFRrq4
Las moléculas de ADN contienen cientos o miles de genes.
Un gen es un segmento de ADN.
El ADN está enrollando formando Cromosomas.
Los genes están formados por nucleótidos.
GEN= PROMOTOR+SECUENCIA_DE_ARN+TERMINADOR

Las señales de inicio y fin (promotor y terminador) son esensenciales para que la ENZIMA ARN POLIMERASA transcriba correctamente los genes y pase por alto las regiones que no lo son.

