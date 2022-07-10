#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import openpyxl as xl


# In[2]:


file_name=input('Enter your file here:-')


# In[3]:


df=pd.read_excel(file_name)
df


# In[4]:


answered=df[['Concept Test 1 - answered','Concept Test 2 - answered','Concept Test 3 - answered','Concept Test 4 - answered','Concept Test 5 - answered','Full Chapter Test 1 - answered',
             'Full Chapter Test 2 - answered','Topic Test 1 - answered','Topic Test 2 - answered']]



# In[5]:


# answered2=answered.iloc[:,[i for i in range(1,10)]]
# answered2
answered2=answered.T


# In[6]:


answered3=pd.melt(answered2)


# In[7]:


answered4=answered3.drop(columns=['variable'])


# In[8]:


df_answered=pd.concat([df,answered4],axis=1)
df_reanswered=df_answered.rename(columns={'value':'answered'})


# In[ ]:





# In[9]:


correct=df[['Concept Test 1- correct','Concept Test 2- correct','Concept Test 3- correct','Concept Test 4- correct','Concept Test 5- correct','Full Chapter Test 1- correct','Full Chapter Test 2- correct','Topic Test 1- correct','Topic Test 2- correct']]
name=df['Name']
correct=correct.set_index(name)
correct=correct.rename(index={'Name':'name'})


# In[10]:


correct2=correct.T


# In[11]:


correct3=pd.melt(correct2)
correct4=correct3.rename(columns={'value':'correct'})



# In[12]:


df_correct=pd.concat([df_answered,correct4],axis=1)


# In[13]:


df_correct2=df_correct.rename(columns={'value':'answered'})


# In[14]:


score=df[['Concept Test 1 - score','Concept Test 2 - score','Concept Test 3 - score','Concept Test 4 - score','Concept Test 5 - score','Full Chapter Test 1 - score','Full Chapter Test 2 - score','Topic Test 1 - score','Topic Test 2 - score']]
id=df['id']
score=score.set_index(id)


# In[15]:


score2=score.T


# In[16]:


score3=pd.melt(score2)


# In[17]:


score4=score3.rename(columns={'value':'score','id':'Username'})


# In[18]:


df_score=pd.concat([df_correct2,score4],axis=1)


# In[19]:


skipped=df[['Concept Test 1- skipped','Concept Test 2- skipped','Concept Test 3- skipped','Concept Test 4- skipped', 'Concept Test 5- skipped','Full Chapter Test 1- skipped','Full Chapter Test 2- skipped','Topic Test 1- skipped','Topic Test 2- skipped']]
test_name=pd.Series(['Concept Test 1','Concept Test 2','Concept Test 3','Concept Test 4','Concept Test 5','Full Chapter Test 1','Full Chapter Test 2','Topic Test 1','Topic Test 2'])


# In[20]:


skipped2=skipped.T



# In[21]:


skipped3=skipped2.reset_index(drop=True)


# In[22]:


skipped4=skipped3.set_index(test_name)
skipped5=skipped4.reset_index(drop=False)



# In[23]:


skipped6=skipped5.melt(id_vars=['index'])


# In[24]:


skipped7=skipped6.drop(columns=['variable'])


# In[25]:


skipped8=skipped7.rename(columns={'index':'Test Name','value':'skipped'})


# In[26]:


df_skipped=pd.concat([df_score,skipped8],axis=1)


# In[27]:


time_taken=df[['Concept Test 1 - time-taken (seconds)','Concept Test 2 - time-taken (seconds)','Concept Test 3 - time-taken (seconds)','Concept Test 4 - time-taken (seconds)','Concept Test 5 - time-taken (seconds)','Full Chapter Test 1 - time-taken (seconds)','Full Chapter Test 2 - time-taken (seconds)','Topic Test 1 - time-taken (seconds)','Topic Test 2 - time-taken (seconds)']]


# In[28]:


time_taken2=time_taken.T


# In[29]:


time_taken3=pd.melt(time_taken2)


# In[30]:


time_taken4=time_taken3.drop(columns=['variable'])


# In[31]:


time_taken5=time_taken4.rename(columns={'value':'time taken(seconds)'})


# In[32]:


df_time_taken=pd.concat([df_skipped,time_taken5],axis=1)


# In[33]:


wrong=df[['Concept Test 1- wrong','Concept Test 2- wrong','Concept Test 3- wrong','Concept Test 4- wrong','Concept Test 5- wrong','Full Chapter Test 1- wrong','Full Chapter Test 2- wrong','Topic Test 1- wrong','Topic Test 2- wrong']]


# In[34]:


wrong2=wrong.T


# In[35]:


wrong3=pd.melt(wrong2)


# In[36]:


wrong3


# In[37]:


wrong4=wrong3.drop(columns=['variable'])


# In[38]:


wrong5=wrong4.rename(columns={'value':'wrong'})


# In[39]:


df_wrong=pd.concat([df_time_taken,wrong5],axis=1)


# In[40]:


df_wrong


# In[41]:


# df2=df_wrong.drop(df_wrong.iloc[:,0:55],axis=1)


# In[42]:


cols=df_wrong.columns
df2=df_wrong.drop(columns=cols[0:57],axis=1)


# In[43]:


df2


# In[44]:


df3=pd.concat([df2,correct4['Name']],axis=1)
len(df3.index)


# In[45]:


value=df.iloc[0,2]


# In[46]:


df3['Chapter Tag'] = pd.Series([value for x in range(len(df3.index+1))])


# In[47]:


df3


# In[48]:


df_reordered = df3.iloc[:, [8, 2, 9, 4, 0, 1, 3, 5, 6, 7]]
df_reordered


# In[49]:


#  df_reshaped = df_reordered[(df_reordered['answered'].str.contains('-')==False),(df_reordered['correct'].str.contains('-')==False),(df_reordered['score'].str.contains('-')==False)or(df_reordered['skipped'].str.contains('-')==False)or
#                                 (df_reordered['time taken(seconds)'].str.contains('-')==False)or(df_reordered['wrong'].str.contains('-')==False)]


# In[50]:


df_reshaped=df_reordered[~df_reordered['score'].isin(['-'])]


# In[51]:


df_reshaped.shape


# In[52]:


df_reshaped.to_excel('Guddu_kumar_output2.xlsx')


# In[53]:


df_reshaped

