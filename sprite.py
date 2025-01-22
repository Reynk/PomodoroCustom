import os
import time

# Delay frames in seconds
delay = 0.1

# ASCII frames (it's supposed to be a cat with a cape running)
fcontent = [
    """
                                       .N:                            
                                      YN2G                            
                              ...,7P7NB  B                            
                         ,rPUNFk12UNBM.  Zr                           
                       .5E2:       1v    ;BU                          
                     :G7r                 v:X7                        
                    LBr                     .0u                       
                   0M                         Br                      
                  Bi                          :B                      
                 02.r15Sk5J7.                  8j                     
                :BrBBB8kOMBBG                  .B                     
               :Ui         .                    0i                    
              7Bi         .                     iP                    
             YB.        :::.                    ,M                    
            .B         ,i.  :.                  .X LSqv.              
            :M         :,,.::.                  :BBBMBBBM,            
            .B          ::::.                  :O0NXqMBMBBu           
             B                               LMBNNEMBB   ,            
             NU                   .UNSBii7PMBBBBBBBBB,                
              B5.                iB:  BGMBOM8BN2U7:.                  
               vBP:              BY  :0    :qi                        
                 r2GBr:.        :B   0u ,YGL                          
                    :7FuNkqLUYL:kL   GBki:                            
                          ..:B: i.   5Bi                              
                             B        .B7                            
                             B,        ,8r                            
                             U1          EB5F7rij772r                 
                             .B          rBMJuvYY;: :F,               
                              uB.  .     B7  .:::iL1L YY              
                              ZYqLrBM.   :0:        BLrBL             
                             :B. ,. iB,   .XL        ::,.             
                              ,J5j:. BBi.   FU                        
                                 .iru,iBr   5U                        
                                       0Zrj5B,                        
                                        ..                            
    """,
    """
                                  .J:  Xq                             
                                 rB;B:ErB                             
                         :LPj51P5BYLBB. 0i                            
                       uB8L:.      .k   UBEi                          
                     YBi.               rE:XPL                        
                    EM.                     .BU                       
                  .BY                         B7                      
                 .B,                          :B                      
                .Bi                            Mu                     
                GU7BBBBBBBBF:                  .B                     
                B  i,....:YB.                   B.                    
              rB7                               B:                    
             :Bi       .:.,                     Z7                    
             B:        i. ..                    8i                    
            LN        ..,...i                   7.                    
            2L        ,:,,..:                   5  .7v8BBB            
            rG         ..:::            .7JUUu2qOO8BBBMMBB            
             Bi                     522BBBBBBBBBO0GNE08BBi            
             :B7                  ,B7..BBBBBBBBBBBBBBBOUi             
              ,GBY.              .Bi  7Y   ;B;7L1PGBGu                
                .U0Pvi.          BL  .BJiYkJ                          
                   .iU5BEXFLkYU7BB   jkri,                            
                         ,:..BY.Br   UN                               
                             B        qZ.                             
                             B.        rBY         :,.                
                             5j          uB2i,,.i7SjLY07              
                             .B.          B8LUrrvr irvuBU             
                             .BB       iBBq1NZir522r:,ruu             
                            M0,N0i77    ,i  :G,                       
                           .B   .rkBBP:      vM                       
                          :Mr   ,Bii iUEuYYuXN;                       
                          FONqBMS.     ..:i..                         
                             .::                                      
    """,
    """
                                   j;                                 
                                 .BrE:,BM                             
                           :iYJuJBMr:N8;B                             
                        YXOJYii::.  ZM  0q.                           
                      v81i         2E   2BZG:                         
                    .ZM            .    7X :BN                        
                   LqL                       NZ                       
                  uB                          08                      
                 :B                            B7                     
                .B.                            ,B                     
                P5 qBBBBBBS.                    B,                    
               vB ::i,i,i7Br                    17                    
              SB.                               Y1                    
             uB         i.,.                    Jk                    
            .B         ; ..,.                   :i                    
            i8        :: :. r               iLL7Ji::                  
            .B        .:,:,.r            rSBBBBBBBBBMB2r:             
             Bi         ,:.:.        ,:UBBBBZLSOBBBBBBBBBB.           
             rB.                   ;BMr7B8,   S  :OBBBBBBBBBU         
              rBu.                :B7  .O   7G;       .YBBB2.         
               .5GPu.            .B:  :M  vB1.                        
                  .r5ZE2Yi;,. i..BY   BZLYj.                          
                      .ir7U2UBqUBO   .B                   w            
                             0,       j2.              w  ww             
                             Mi        ;Br          ,77ww w             
                             Fw2          8Z7Y2kSXrvXE:.Bj    
                            ASD,0i77    ,i  :G,                       
                           .B   .rkBBP:      vM                       
                          :MSdr   ,BqwdwdefrYYuxee;                       
                          awdafewf.     ..:ddda.                         
                             .ass                        
    """
]

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ascii_art():
    """Animates ASCII art frames with a delay."""
    index = 0
    while True:
        clear_screen()
        print(fcontent[index])
        index = (index + 1) % len(fcontent)  # Cycle through frames
        time.sleep(delay)

# run
if __name__ == "__main__":
    animate_ascii_art()