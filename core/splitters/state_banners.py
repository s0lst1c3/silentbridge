upstream_connected = ''' 
  authenticator
       |
   ---------
   |       |
   x       |
           |
   x       |
   |       | '''

upstream_bypass = '''
  authenticator
       |
   ---------
   |       |
   |       x
   |
   |       x
   |       | '''

banner_center = '''   |     upstream
   |       |
   |    silentbridge
   |       |
   |      phy '''
phy_connected = '''   |       |
   x       |
           |
   x       |
   |       |
   ---------
       |
   supplicant
'''

phy_bypass = '''   |       |
   |       x
   |
   |       x
   |       |
   ---------
       |
   supplicant
'''
