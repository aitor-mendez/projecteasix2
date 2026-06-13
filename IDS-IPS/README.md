Aquí trobareu la configuració del pfSense que he fet servir per a dur a terme aquest projecte, el qual porta instal·lat el Suricata, l'IDS/IPS escollit.

Si poseu "Suricata" al cercador del fitxer, trobareu les línies de configuració d'aquest.

El bloc principal de Suricata es troba a la línia 819. Aquí es on veureu la configuració de les interfícies, de les regles i dels logs.

Per importar la configuració al vostre pfSense, heu d'anar a Diagostics > Backup & Restore i fer el següent:
1. A Restore Area, escolliu "All"
2. A Configuration File, escolliu el fitxer de configuració.
3. Feu clic a "Restore Configuration"
