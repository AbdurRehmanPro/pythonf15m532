#includestdio.h
#includegraphics.h
struct terms        CREATTING A STRUCTURE
{
  char process_name[20];
  int arrival_time;
  int burst_time;
  int exit_time;
  int waiting_time;
  int turn_arrival;
  int rest_burst;
  int execution_start;
  int execution_end;
};
main()
{
    printf(Enter the number of process that you haven);
    int n;
    scanf(%d,&n);
   struct terms st[n];
    int i;
                                     TAKING INPUT
    for(i=0;in;i++)
    {
        printf(Enter the name of your %d processn,(i+1));
        scanf(%s,st[i].process_name);
        printf(Enter the Arrival time of your %d processn,(i+1));
        scanf(%d,&st[i].arrival_time);
         printf(Enter the Burst time of your %d processn,(i+1));
        scanf(%d,&st[i].burst_time);
    }
                                  CALCULATING THE VALUES OF VERIABLES
    for(i=0;in;i++)
    {
        if(i==0)
        {
            st[i].execution_start=st[0].arrival_time;
            st[i].execution_end=st[0].arrival_time+st[0].burst_time;
        }
        else
        {
        st[i].execution_start=st[i-1].execution_end;
        st[i].execution_end=st[i].execution_start+st[i].burst_time;
        }
        st[i].rest_burst=st[i].burst_time-(st[i].execution_end-st[i].execution_start);

    }
    for(i=0;in;i++)
    {
        st[i].exit_time=st[i].execution_end;
        st[i].turn_arrival=st[i].exit_time-st[i].arrival_time;
        st[i].waiting_time=st[i].turn_arrival-st[i].burst_time;

    }
     float sum=0;
    for(i=0;in;i++)
    sum=sum+st[i].waiting_time;
    sum=sumn;
    printf(Average Waiting Time= %f,sum);
    printf(nnnPress ENTER For Graphical viewnn);
    system(pause);
                      CREATING TABLE FOR QUESTION AND execution

     initwindow(800,500,powered by deepak yadav,0,0,false,true);
     int x=100;
     int y=40;
     setcolor(YELLOW);
     outtextxy(0,1,Question table--);
     outtextxy(440,1,Execution table--);
     for(i=0;i(n+2);i++)
        {
            line(0,y,300,y);
            Sleep(100);
            line(400,y,800,y);
            y=y+40;
            Sleep(100);
        }
    for(i=0;i8;i++)
    {
        Sleep(100);
        line(x,40,x,(n+2)40);
        x=x+100;
    }
    setcolor(GREEN);
    outtextxy(10,50,Process);
    Sleep(100);
    outtextxy(105,50,Arrival_Time);
    Sleep(100);
    outtextxy(205,50,Burst_Time);
    Sleep(100);
    outtextxy(410,50,Process);
    Sleep(100);
    outtextxy(500,50,execution_Time);
    Sleep(100);
    outtextxy(610,50,Rest_Burst);
    Sleep(100);
    outtextxy(720,50,State);
    Sleep(100);
     char str[20];
     char str2[]=Exit;
     char str3[]=Waiting;
                           PUTTING THE VALUES OF VERIABLES IN QUESTION TABLE
     x=40;
     y=90;
     setcolor(WHITE);
     for(i=0;in;i++)
     {
         outtextxy(x,y,st[i].process_name);
         Sleep(100);
         sprintf(str,%d,st[i].arrival_time);
         Sleep(100);
         outtextxy(x+100,y,str);
         Sleep(100);
         sprintf(str,%d,st[i].burst_time);
         Sleep(100);
         outtextxy(x+200,y,str);
         Sleep(100);
         y=y+40;
     }
                          PUTTING THE VALUES OF VERIABLES IN execution TABLE
     x=440;
     y=90;
      for(i=0;in;i++)
     {
         outtextxy(x,y,st[i].process_name);
         Sleep(100);
         sprintf(str,%d - %d,st[i].execution_start,st[i].execution_end);
         Sleep(100);
         outtextxy(x+80,y,str);
         Sleep(100);
         sprintf(str,%d,st[i].rest_burst);
         Sleep(100);
         outtextxy(x+200,y,str);
         Sleep(100);
         if(st[i].rest_burst==0)
         outtextxy(x+300,y,Exit);
          else
            outtextxy(x+300,y,Waiting);
         y=y+40;
         Sleep(100);
     }
     outtextxy(1,480,Press Any key to view Final Output table);
     getch();
     cleardevice();
                               CREATING TABLE FOR FINAL OUTPUT
      x=100;
      y=40;
      setcolor(YELLOW);
      outtextxy(0,1,Final Output table--);
      for(i=0;i(n+2);i++)
        {
            Sleep(100);
            line(0,y,600,y);

            y=y+40;
        }
    for(i=0;i6;i++)
    {
         Sleep(100);
        line(x,40,x,(n+2)40);
        x=x+100;
    }
    setcolor(GREEN);
    outtextxy(10,50,Process);
    Sleep(100);
    outtextxy(105,50,Arrival_Time);
    Sleep(100);
    outtextxy(205,50,Exit_Time);
    Sleep(100);
    outtextxy(310,45,Turn_Arrival);
    Sleep(100);
    outtextxy(330,60,Time);
    Sleep(100);
    outtextxy(410,50,Burst_Time);
    Sleep(100);
    outtextxy(510,50,Waiting_Time);
    Sleep(100);
                                    PUTTING THE VALUES OF VERIABLES IN OUTPUT TABLE
     x=40;
     y=90;
     setcolor(15);
     for(i=0;in;i++)
     {
         outtextxy(x,y,st[i].process_name);
         Sleep(100);
         sprintf(str,%d,st[i].arrival_time);
         Sleep(100);
         outtextxy(x+100,y,str);
         sprintf(str,%d,st[i].exit_time);
         Sleep(100);
         outtextxy(x+200,y,str);
         sprintf(str,%d,st[i].turn_arrival);
         Sleep(100);
         outtextxy(x+300,y,str);
         sprintf(str,%d,st[i].burst_time);
         Sleep(100);
         outtextxy(x+400,y,str);
         sprintf(str,%d,st[i].waiting_time);
         Sleep(100);
         outtextxy(x+500,y,str);
         Sleep(100);
         y=y+40;
     }
     outtextxy(1,480,Press Any key to view Gantt Chart);
     getch();
     cleardevice();
     char str4[50];
     setcolor(YELLOW);
     sprintf(str4,Average Waiting Time = %f,sum);
     outtextxy(0,50,str4);
     x=3;
     y=200;
     outtextxy(0,160,Gantt Chart-);
     setcolor(YELLOW);
     for(i=0;in;i++)
     {
         Sleep(100);
         rectangle(x,y,x+50,y+50);
         x=x+50;
     }
     x=1;
     y=184;
     setcolor(15);
     for(i=0;in;i++)
     {
         if(i==0)
         {
             Sleep(100);
              sprintf(str,%d,st[i].execution_start);
              outtextxy(x,y,str);
              x=x+48;
         }
         {
             Sleep(100);
              sprintf(str,%d,st[i].execution_end);
              outtextxy(x,y,str);
               x=x+48;
         }
     }
     x=20;
     y=215;
     for(i=0;in;i++)
     {
         Sleep(100);
         outtextxy(x,y,st[i].process_name);
         x=x+48;
     }
getch();
}