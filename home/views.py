from django.shortcuts import render, redirect, get_object_or_404

from .models import Player, Team, PlayerPosition
import csv
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from .forms import RegistroForm

from selenium import webdriver
import time
import unidecode
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By
# Create your views here.


class Sofascore_Scraper:
      
      impicitlyWaitTime = 1
      sleepTime = 1
      sleep = True

      def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--headless')  # ----> Opcion de driver para ejecutarlo  sin abrir el navegador
        #options.add_argument('--no-sandbox')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # options.add_argument("user-data-dir=selenium")
        self.options.add_argument("--remote-debugging-port=9222")
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-site-isolation-trials')

        self.driver = webdriver.Chrome(executable_path = r"C:\\Users\\marcl\\drivers\\chromedriver_win32\\chromedriver.exe", options = self.options)
        
        self.act = ActionChains(self.driver)
        self.driver.maximize_window()

      def sleep(self):
       if self.sleep == True:
        time.sleep(self.sleepTime)

      def render(self):
        for i in range(1,25):
         self.act.send_keys(Keys.SPACE).perform()
        for i in range(1,125):
         self.act.send_keys(Keys.UP).perform()
         
      def register_football_team(self):
          
          self.driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
          self.sleep()
          cookies = self.driver.find_element(By.XPATH, '//*[text()="Consentir"]')
          self.act.move_to_element(cookies).click().perform()
          
          for x in range(1,21):
                    
            self.render()
                
            try:  
                self.driver.implicitly_wait(self.impicitlyWaitTime)
                team_element = self.driver.find_element(By.XPATH, f'//div[@class="sc-csuSiG ikkoci"]/div/a[{x}]/div[1]/div[3]/div/span').text
                self.sleep()
                    
            except:
                
                continue
            
            s = team_element.replace(" ", "-" )
           
            sl = unidecode.unidecode(s)
                
              
            slug = sl.lower()
                    
            team = Team(name=team_element, slug=slug)
            team.save()
            self.sleep()
            
          self.driver.close()
                    
                    
          
      def register_football_players(self): 
            
            self.driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
            self.sleep()
            cookies = self.driver.find_element(By.XPATH, '//*[text()="Consentir"]')
            self.act.move_to_element(cookies).click().perform()
            
            for x in range(1,21):
                    
                    self.render()
                        
                    try:  
                            
                        self.driver.implicitly_wait(self.impicitlyWaitTime)
                        team_element = self.driver.find_element(By.XPATH, f'//div[@class="sc-csuSiG ikkoci"]/div/a[{x}]')
                        team_og = self.driver.find_element(By.XPATH, f'//div[@class="sc-csuSiG ikkoci"]/div/a[{x}]/div[1]/div[3]/div/span').text
                        self.sleep()
                            
                    except:
                        
                        continue
                    
                    team_link = team_element.get_attribute('href')
                    self.driver.get(team_link)
                    self.sleep()

                    self.render()

                    

                    for y in range(35):

                        try:
                            
                            self.driver.implicitly_wait(self.impicitlyWaitTime)
                            player = self.driver.find_elements(By.CLASS_NAME, 'sc-hLBbgP.kIfRA')[y]
                            self.sleep()
                            
                        except:
                            continue
                        
                        
                        link = player.find_element(By.TAG_NAME, 'a').get_attribute('href')

                        self.driver.get(link)
                        self.sleep()
                        
                        self.render()

                        try:
                            name = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[1]/div[2]/div[1]/div[1]/div[2]/h2').text

                        except:
                            name = ''
                        
                        try:
                            team = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[1]/a/div/div/div').text

                        except:
                            team = ''
                    
                        
                        try:
                            nationality = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/span').text
                        except:
                            nationality = ""
                        
                        try:
                            age = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[2]/div[2]').text
                        except:
                            age = ""
                        
                        try:
                            altura = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[3]/div[2]').text
                        except:
                            altura = ""
                            
                        try:
                            foot = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[4]/div[2]').text
                        except:
                            foot = ""
                            
                        try:
                            position = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[5]/div[2]').text
                        except:
                            position = ""
                            
                        try:
                            number = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[6]/div[2]').text
                        except:
                            number = ""
                            
                        slug = name.replace(" ", "-" )
                        
                        print(name)
                        
                        if position == 'F':
                            pos = "Delantero"
                        elif position == 'M':
                            pos = "Mediocentro"
                        elif position == 'D':
                            pos = "Defensa"
                        else:
                            pos = "Portero"
                            
                        if team != team_og:
                            team = team_og
                            
                        player = Player(
                                    name=name, 
                                    team=Team.objects.get(name=team), 
                                    position=PlayerPosition.objects.get(name=pos),
                                    nationality=nationality, 
                                    age=age, 
                                    altura=altura, 
                                    foot=foot, 
                                    number=number,
                                    slug=slug,
                                    )
                        
                        player.save()  
                        self.sleep()
                        
                        
                        self.driver.implicitly_wait(self.impicitlyWaitTime)
                        self.driver.back()
                        self.sleep()
                
                
                
            
                    self.driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
                    self.sleep()
                
            self.driver.close() 
               
                
                
          
          
      def scrap_total_stats(self):
          
        self.driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
        self.sleep()
        cookies = self.driver.find_element(By.XPATH, '//*[text()="Consentir"]')
        self.act.move_to_element(cookies).click().perform()
        
        
            
                
        for x in range(1,21):
            
            self.render()
                
            try:  
                    
                self.driver.implicitly_wait(self.impicitlyWaitTime)
                team_element = self.driver.find_element(By.XPATH, f'//div[@class="sc-csuSiG ikkoci"]/div/a[{x}]')
                team_og = self.driver.find_element(By.XPATH, f'//div[@class="sc-csuSiG ikkoci"]/div/a[{x}]/div[1]/div[3]/div/span').text
                self.sleep()
                    
            except:
                
                continue
            
            team_link = team_element.get_attribute('href')
            self.driver.get(team_link)
            self.sleep()

            self.render()

            

            for y in range(35):

                try:
                    
                    self.driver.implicitly_wait(self.impicitlyWaitTime)
                    player = self.driver.find_elements(By.CLASS_NAME, 'sc-hLBbgP.kIfRA')[y]
                    self.sleep()
                    
                except:
                    continue
                
                
                link = player.find_element(By.TAG_NAME, 'a').get_attribute('href')

                self.driver.get(link)
                self.sleep()
                
                self.render()

                try:
                    name = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[1]/div[2]/div[1]/div[1]/div[2]/h2').text

                except:
                    name = ''
                
                
                s = name.replace(" ", "-" )
           
                sl = unidecode.unidecode(s)
                
              
                slug = sl.lower()
                    
                
                try:
                    team = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[1]/a/div/div/div').text

                except:
                    team = ''
            
                
                try:
                    nationality = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/span').text
                except:
                    nationality = ""
                
                try:
                    age = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[2]/div[2]').text
                except:
                    age = ""
                
                try:
                    altura = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[3]/div[2]').text
                except:
                    altura = ""
                    
                try:
                    foot = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[4]/div[2]').text
                except:
                    foot = ""
                    
                try:
                    position = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[5]/div[2]').text
                except:
                    position = ""
                    
                try:
                    number = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP fSpQRs sc-836c558d-2 kBACDz"]/div[2]/div[1]/div[2]/div[6]/div[2]').text
                except:
                    number = ""
                    
    
    
            
                try:
                    matches_played = self.driver.find_element(By.XPATH, '//div[span/text()="Total played"]/span[2]').text
                except:
                    matches_played = ""
                
                try:
                    started = self.driver.find_element(By.XPATH, '//div[span/text()="Started"]/span[2]').text
                except:
                    started = ""
                
                try:
                    minutes_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Minutes per game"]/span[2]').text
                except:
                    minutes_pg = ""
                
                
                self.driver.implicitly_wait(self.impicitlyWaitTime)
                
                try:
                    goals = self.driver.find_element(By.XPATH, '//div[@class="sc-hLBbgP gMIWmD sc-836c558d-2 bvjPFc"]/div[1]/div[5]/div[2]/div[2]/div[1]/span[2]').text
                except:
                    goals = ""
                
                try:
                    xgoals = self.driver.find_element(By.XPATH, '//div[span/text()="Expected Goals (xG)"]/span[2]').text
                except:
                    xgoals = ""
                
                
                
                try:
                    score_freq = self.driver.find_element(By.XPATH, '//div[span/text()="Scoring frequency"]/span[2]').text
                except:
                    score_freq = "" 
                
                
                
                try:
                    goalspg = self.driver.find_element(By.XPATH, '//div[span/text()="Goals per game"]/span[2]').text
                except:
                    goalspg = ""
                
                
                try:
                    shotspg = self.driver.find_element(By.XPATH, '//div[span/text()="Shots per game"]/span[2]').text
                except:
                    shotspg = ""
                
                try:
                    shots_ontargetpg = self.driver.find_element(By.XPATH, '//div[span/text()="Shots on target per game"]/span[2]').text
                except:
                    shots_ontargetpg = ""
                
                try:
                    bigchances_missed = self.driver.find_element(By.XPATH, '//div[span/text()="Big chances missed"]/span[2]').text
                except:
                    bigchances_missed = ""
                
                try:
                    goal_conversion = self.driver.find_element(By.XPATH, '//div[span/text()="Goal conversion"]/span[2]').text
                except:
                    goal_conversion = ""
                
                try:
                    fk_goals = self.driver.find_element(By.XPATH, '//div[span/text()="Free kick goals"]/span[2]').text
                except:
                    fk_goals = ""
                
                try:
                    fk_conversion = self.driver.find_element(By.XPATH, '//div[span/text()="Free kick conversion"]/span[2]').text
                except:
                    fk_conversion = ""
                
                try:
                    goals_insidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Goals from inside the box"]/span[2]').text
                except:
                    goals_insidebox = ""
                
                try:
                    goals_outsidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Goals from outside the box"]/span[2]').text
                except:
                    goals_outsidebox = ""
                
                try:
                    headed_goals = self.driver.find_element(By.XPATH, '//div[span/text()="Headed goals"]/span[2]').text
                except:
                    headed_goals = ""
                
                try:
                    leftf_goals = self.driver.find_element(By.XPATH, '//div[span/text()="Left foot goals"]/span[2]').text
                except:
                    leftf_goals = ""
                
                try:
                    rightf_goals = self.driver.find_element(By.XPATH, '//div[span/text()="Right foot goals"]/span[2]').text
                except:
                    rightf_goals = ""
                
                try:
                    penalty_won = self.driver.find_element(By.XPATH, '//div[span/text()="Penalty won"]/span[2]').text
                except:
                    penalty_won = ""
                
                
                try:
                    assists = self.driver.find_element(By.XPATH, '//div[span/text()="Assists"]/span[2]').text
                except:
                    assists = ""
                
                try:
                    xassists = self.driver.find_element(By.XPATH, '//div[span/text()="Expected Assists (xA)"]/span[2]').text
                except:
                    xassists = ""
                
                try:
                    touches = self.driver.find_element(By.XPATH, '//div[span/text()="Touches"]/span[2]').text
                except:
                    touches = ""
                
                try:
                    bigchances_created = self.driver.find_element(By.XPATH, '//div[span/text()="Big chances created"]/span[2]').text
                except:
                    bigchances_created = ""
                
                
                try:
                    key_passes = self.driver.find_element(By.XPATH, '//div[span/text()="Key passes"]/span[2]').text
                except:
                    key_passes = ""
                
                try:
                    acc_pergame = self.driver.find_element(By.XPATH, '//div[span/text()="Accurate per game"]/span[2]').text
                except:
                    acc_pergame = ""
                
                try:
                    acc_ownhalf = self.driver.find_element(By.XPATH, '//div[span/text()="Acc. own half"]/span[2]').text
                except:
                    acc_ownhalf = ""
                
                
                try:
                    acc_oppohalf = self.driver.find_element(By.XPATH, '//div[span/text()="Acc. opposition half"]/span[2]').text
                except:
                    acc_oppohalf = ""
                
                try:
                    acc_longballs = self.driver.find_element(By.XPATH, '//div[span/text()="Acc. long balls"]/span[2]').text
                except:
                    acc_longballs = ""
                
                try:
                    acc_chipballs = self.driver.find_element(By.XPATH, '//div[span/text()="Acc. chipped passes"]/span[2]').text
                except:
                    acc_chipballs = ""
                
                try:
                    acc_crosses = self.driver.find_element(By.XPATH, '//div[span/text()="Acc. crosses"]/span[2]').text
                except:
                    acc_crosses = ""
                
                
                try:
                    interceptions_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Interceptions per game"]/span[2]').text
                except:
                    interceptions_pg = ""
                
                try:
                    tackles_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Tackles per game"]/span[2]').text
                except:
                    tackles_pg = ""
                
                try:
                    poss_won = self.driver.find_element(By.XPATH, '//div[span/text()="Possession won"]/span[2]').text
                except:
                    poss_won = ""
                
                try:
                    dribbled_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Dribbled past per game"]/span[2]').text
                except:
                    dribbled_pg = ""
                
                try:
                    clearences_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Clearances per game"]/span[2]').text
                except:
                    clearences_pg = ""
                
                try:
                    error_leadtoshot = self.driver.find_element(By.XPATH, '//div[span/text()="Error led to shot"]/span[2]').text
                except:
                    error_leadtoshot = ""
                
                try:
                    error_leadtogoal = self.driver.find_element(By.XPATH, '//div[span/text()="Error led to goal"]/span[2]').text
                except:
                    error_leadtogoal = ""
                
                try:
                    penalties_commited = self.driver.find_element(By.XPATH, '//div[span/text()="Penalties committed"]/span[2]').text
                except:
                    penalties_commited = ""
                
                
                try:
                    succ_dribbles = self.driver.find_element(By.XPATH, '//div[span/text()="Succ. dribbles"]/span[2]').text
                except:
                    succ_dribbles = ""
                
                try:
                    total_duelswon = self.driver.find_element(By.XPATH, '//div[span/text()="Total duels won"]/span[2]').text
                except:
                    total_duelswon = ""
                
                try:
                    ground_duelswon = self.driver.find_element(By.XPATH, '//div[span/text()="Ground duels won"]/span[2]').text
                except:
                    ground_duelswon = ""
                
                try:
                    air_duelswon = self.driver.find_element(By.XPATH, '//div[span/text()="Aerial duels won"]/span[2]').text
                except:
                    air_duelswon = ""
                
                try:
                    poss_lost = self.driver.find_element(By.XPATH, '//div[span/text()="Possession lost"]/span[2]').text
                except:
                    poss_lost = ""
                
                try:
                    fouls_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Fouls"]/span[2]').text
                except:
                    fouls_pg = ""
                
                try:
                    fouled_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Was fouled"]/span[2]').text
                except:
                    fouled_pg = ""
                
                try:
                    offsides = self.driver.find_element(By.XPATH, '//div[span/text()="Offsides"]/span[2]').text
                except:
                    offsides = ""
                
                
                try:
                    yellows = self.driver.find_element(By.XPATH, '//div[span/text()="Yellow"]/span[2]').text
                except:
                    yellows = ""
                
                try:
                    doble_yellows = self.driver.find_element(By.XPATH, '//div[span/text()="Yellow-Red"]/span[2]').text
                except:
                    doble_yellows = ""
                
                try:
                    reds = self.driver.find_element(By.XPATH, '//div[span/text()="Red cards"]/span[2]').text
                except:
                    reds = ""
                
                
                
                try:
                    penalty_goals = self.driver.find_element(By.XPATH, '//div[span/text()="Penalty goals"]/span[2]').text
                except:
                    penalty_goals = ""
                
                try:
                    penalty_conversion = self.driver.find_element(By.XPATH, '//div[span/text()="Penalty conversion"]/span[2]').text
                except:
                    penalty_conversion = ""
                
                try:
                    goals_concededpg = self.driver.find_element(By.XPATH, '//div[span/text()="Goals conceded per game"]/span[2]').text
                except:
                    goals_concededpg = ""
                try:
                    pens_saved = self.driver.find_element(By.XPATH, '//div[span/text()="Penalties saved"]/span[2]').text
                except:
                    pens_saved = ""
                    
                try:
                    saves_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Saves per game"]/span[2]').text
                except:
                    saves_pg = ""
                    
                try:
                    succruns_pg = self.driver.find_element(By.XPATH, '//div[span/text()="Succ. runs out per game"]/span[2]').text
                except:
                    succruns_pg = ""
                    
                try:
                    goals_conceded = self.driver.find_element(By.XPATH, '//div[span/text()="Goals conceded"]/span[2]').text
                except:
                    goals_conceded = ""
                    
                try:
                    conceded_insidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Conceded from inside box"]/span[2]').text
                except:
                    conceded_insidebox = ""
                    
                try:
                    conceded_outsidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Conceded from outside box"]/span[2]').text
                except:
                    conceded_outsidebox = ""
                    
                try:
                    saves_made = self.driver.find_element(By.XPATH, '//div[span/text()="Saves made"]/span[2]').text
                except:
                    saves_made = ""
                    
                try:
                    goals_prevented = self.driver.find_element(By.XPATH, '//div[span/text()="Goals prevented"]/span[2]').text
                except:
                    goals_prevented = ""
                    
                try:
                    saves_insidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Saves from inside box"]/span[2]').text
                except:
                    saves_insidebox = ""
                    
                try:
                    saves_outsidebox = self.driver.find_element(By.XPATH, '//div[span/text()="Saves from outside box"]/span[2]').text
                except:
                    saves_outsidebox = ""
                    
                try:
                    saves_caught = self.driver.find_element(By.XPATH, '//div[span/text()="Saves caught"]/span[2]').text
                except:
                    saves_caught = ""
                    
                try:
                    saves_parried = self.driver.find_element(By.XPATH, '//div[span/text()="Saves parried"]/span[2]').text
                except:
                    saves_parried = ""
                    
                print(name)
                
                if position == 'F':
                    pos = "Delantero"
                elif position == 'M':
                    pos = "Mediocentro"
                elif position == 'D':
                    pos = "Defensa"
                else:
                    pos = "Portero"
                    
                if team != team_og:
                    team = team_og
                    
                player = Player(
                            name=name, 
                            team=Team.objects.get(name=team), 
                            position=PlayerPosition.objects.get(name=pos),
                            nationality=nationality, 
                            age=age, 
                            altura=altura, 
                            foot=foot, 
                            number=number,
                            slug=slug,
                            matches=matches_played,
                            started=started,
                            min_per_game=minutes_pg,
                            goals=goals,
                            exp_goals=xgoals,
                            penalty_goals=penalty_goals,
                            penalty_conversion=penalty_conversion,
                            score_freq=score_freq,
                            goals_per_game=goalspg,
                            
                            shots_per_game=shotspg,
                            
                            shots_on_target_per_game=shots_ontargetpg,
                            bigchances_missed=bigchances_missed,
                            goal_conversion=goal_conversion,
                            freekick_goals=fk_goals,
                            freekick_conversion=fk_conversion,
                            goals_insidebox=goals_insidebox,
                            goals_outsidebox=goals_outsidebox,
                            head_goals=headed_goals,
                            left_goals=leftf_goals,
                            right_goals=rightf_goals,
                            penalty_won=penalty_won,
                            assists=assists,
                            exp_assists=xassists,
                           
                            touches_per_game=touches,
                            bigchances_created=bigchances_created,
                            
                            key_passes_per_game=key_passes,
                            
                            acc_per_game=acc_pergame,
                            
                            acc_own_half=acc_ownhalf,
                            
                            acc_oppo_half=acc_oppohalf,
                           
                            acc_longballs=acc_longballs,
                            
                            acc_chipballs=acc_chipballs,
                            
                            acc_crosses=acc_crosses,
                            
                            intercep_per_game=interceptions_pg,
                            tackles_per_game=tackles_pg,
                            poss_won=poss_won,
                            dribbled_per_game=dribbled_pg,
                            
                            clearences_per_game=clearences_pg,
                            errors_leadtoshot=error_leadtoshot,
                            errors_leadtogoal=error_leadtogoal,
                            penalty_commited=penalties_commited,
                            
                            succ_dribbles_per_game=succ_dribbles,
                            
                            duels_won_per_game=total_duelswon,
                            
                            ground_duels_won_per_game=ground_duelswon,
                            
                            air_duels_won_per_game=air_duelswon,
                           
                            poss_lost_per_game=poss_lost,

                            fouls_per_game=fouls_pg,
                            fouled_per_game=fouled_pg,
                            yellows=yellows,
                            yellow_reds=doble_yellows,
                            reds=reds,
                            
                            )
                
                player.save()  
                self.sleep()
                    
                
                
                self.driver.implicitly_wait(self.impicitlyWaitTime)
                self.driver.back()
                self.sleep()
        
        
        
    
            self.driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
            self.sleep()
        
        self.driver.close() 
        
                        
                

class AdminViews():
 
    @staff_member_required
    def actualitzar_dades(request):
        if request.method == 'POST':
        
            if request.POST.get("form_type") == 'Teams':
                scraper = Sofascore_Scraper()
                scraper.register_football_team()
                messages.info(
                request, 'Equips registrats correctament.')
            
            elif request.POST.get("form_type") == 'Players':
                
                scraper = Sofascore_Scraper()
                scraper.scrap_total_stats()
                messages.info(
                request, 'Jugadors registrats correctament.')
                
            elif request.POST.get("form_type") == 'Borrar':
                
                Team.objects.all().delete()
                messages.info(
                request, 'Dades borrades correctament.')
                
        
        return render(request, 'home/admin/form.html')
    
    
    def registro(request):
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
            
            return redirect('/')
        else:
            form = RegistroForm()
        
        
        return render(request, 'home/registro/registro.html', {'form': form})
    

class AppViews():
    
    def home(request):
        
        return render(request, 'home/app/equipo.html')
    
    def player_detail(request, slug):
      
        player = get_object_or_404(Player, slug=slug, is_active=True)
        return render(request, 'home/app/player.html', {'player': player})
    
    def position_player(request, position_slug):
      
        position = get_object_or_404(PlayerPosition, slug=position_slug)
        players = Player.objects.filter(position=position)
        return render(request, 'home/app/position.html', {'position': position, 'players': players})

        
    def players(request):
        
        players = Player.objects.all()
        return render(request, 'home/app/players.html', {'players': players})