#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>


#define COMMAND_LENGTH 10
#define NAME_LENGTH 20
#define PASSWORD_LENGTH 40
#define MAX_PSWD 100

#define OK_CODE 1
#define NOPE_CODE 2
#define ERR_CODE 3

struct pswd_object{
    char* service;
    char* password;

    //number of checking
    //valid
    //ecc.

}pswds[MAX_PSWD];    //array pf password

int n_pswd;
//todo: make it array


// ----------------------------------------------- //
//                  UTILITY FUNCTIONS
// ----------------------------------------------- //

int find_service(char* service){
    for(int i=0; i<n_pswd; i++){
        if(!strcmp(pswds[i].service, service))
            return OK_CODE;
    }
    return NOPE_CODE;
}


void prompt(){
    printf("\n> ");
    fflush(stdout);
}


// ----------------------------------------------- //
//                  COMMANDS FUNCTIONS
// ----------------------------------------------- //

void help_command(){
    printf("Try any of the following commands:\n\n"
        "1) help: show commands details\n"
        "2) list: show all passwprd list\n"
        "3) save: save new passwprd\n"
        //todo: add others
    );


}

void boot_command(){
    printf("\nWelcome in pswdman!\n");
    help_command();
}


void esc_command(){
    exit(0);
}

void list_command(){
    printf("\t#\tname\tpassword\n");
    for(int i=0; i<n_pswd; i++){
        printf("\t%d\t%s\t%s\n", i, pswds[i].service, pswds[i].password);
    }


}

int save_command(){
    if(n_pswd >= MAX_PSWD)
        return ERR_CODE;

    printf("Insert service you want to save a password for: \n");
    char name[NAME_LENGTH];
    scanf("%s", name);

    find_service(name);

    char password[PASSWORD_LENGTH];
    char confirm[PASSWORD_LENGTH];

    bool ok = false;

    while(!ok){
        printf("Insert password and confirmation: \n");
        scanf("%s", password);
        scanf("%s", confirm); 

        if(strcmp(password, confirm))
            printf("password dont match: retry\n");
        else
            ok = true;
    }        

    struct pswd_object* p = &pswds[n_pswd++];

    p->service = malloc(sizeof(name)+1);
    p->password = malloc(sizeof(password)+1);
    strcpy(p->service, name);
    strcpy(p->password, password);
    

    return OK_CODE;
}

void read_command(){

    prompt();

    char cmd[COMMAND_LENGTH];
    scanf("%s", cmd);

    if(!strncmp(cmd, "clear", 4) || !strncmp(cmd, "cls", 3)){
        system("clear");
        return;
    }

    if(!strncmp(cmd, "esc", 3)){
        esc_command();
        return;
    }
    if(!strncmp(cmd, "help", 4)){
        help_command();
        return;
    }
    if(!strncmp(cmd, "list", 4)){
        list_command();
        return;
    }
    if(!strncmp(cmd, "save", 4)){
        save_command();
        return;
    }

    printf("Command not found!\n");
    help_command();

}


