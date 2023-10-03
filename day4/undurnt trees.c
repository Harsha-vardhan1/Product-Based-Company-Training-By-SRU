/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int info;
    struct node *next;
};
struct node *head=NULL;
void insertatbegin()
{
    struct node *newnode;
    newnode=(struct node *)malloc(sizeof(struct node));
    int d;
    scanf("%d",&d);
    newnode->info=d;
    newnode->next=NULL;
    if(head==NULL)
    {
        head=newnode;
    }
    else
    {
        newnode->next=head;
        head=newnode;
    }
    
}
void deleteatbegin()
{
    struct node *temp;
    temp=head;
  if (head==NULL)
  {
      head=NULL;
  }
    else{
        head=head->next;
    }
}
void insertatend()
{
    int d;
    scanf("%d",&d);
    struct node *temp;
    temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    struct node *newnode;
    newnode=(struct node *)malloc(sizeof(struct node));
    newnode->info=d;
    newnode->next=NULL;
    if(head==NULL)
    {
        head=newnode;
    }
    else
    {
        temp->next=newnode;
    }
    
}
void deleteatend()
{
    struct node *temp,*ptr;
    temp=head;
    
    while(temp->next!=NULL)
    {ptr=temp;
        temp=temp->next;
    }
    ptr->next=NULL;
}
void insertatspec()
{
    int p,d;
    printf("Enter the position and data");
    scanf("%d %d",&p,&d);
    struct node *newnode,*prev,*temp;
    newnode=(struct node *)malloc(sizeof(struct node));
    newnode->next=NULL;
    newnode->info=d;
    int i=0;
    temp=head;
    prev=head;
   while(temp!=NULL&&i!=p)
   {
       i++;
       prev=temp;
       temp=temp->next;
   }
    prev->next=newnode;
    newnode->next=temp;
    
}
void traverse()
{
    struct node *temp;
    temp=head;
    while(temp!=NULL)
    {
        printf("%d ",temp->info);
        temp=temp->next;
    }
}
void deleteatspe()
{
    struct node *temp,*ptr;
    temp=head;
    int loc,i=0;
    scanf("%d",&loc);
    while(temp!=NULL && i+1!=loc)
    {i++;
        ptr=temp;
        temp=temp->next;
    }
    ptr->next=temp->next;
}
int main()
{
    insertatbegin();
    insertatbegin();
    insertatend();
    insertatend();
    insertatspec();
    deleteatbegin();
    deleteatend();
    traverse();
    deleteatspe();
    traverse();
    return 0;
}
