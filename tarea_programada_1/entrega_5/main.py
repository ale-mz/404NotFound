import analyzer

# TODO: cambiar cuando se cambie el algoritmo de graficas
import matplotlib.pyplot as plt

if __name__ == "__main__":
  output = []
  output = analyzer.analyze("vpn-logs-2020-modified-abb-revMM.txt")
  # for i in range(len(output)):
  #   print(output[i])

  # print("\n")

  vpns = []
  vpns = analyzer.vpn_table()
  # for i in range(len(vpns)):
  #   print(vpns[i])

  # print("\n")

  conn = []
  conn = analyzer.vpn_con()
  # for i in range(len(conn)):
  #   print(conn[i])


  # ------------------ Make a function -----------
  dataframe = []
  print("\n")

  # Pass all to a new table
  for i in range(len(output)):

    # Look if the user was previously append
    userbool = False
    for j in range(len(dataframe)):
      if (dataframe[j][1] == output[i][1]):
        userbool = True
      
    if userbool == False:
      # IP(s)
      IPs = [output[i][2]]
      # Route(s) list
      RTs = [output[i][3]]

      # Append to the new table all data from the old one
      # Bool / User / IP(s) / Route(s) / Conection(s) / #IP(s) / #Route(s)
      input = [output[i][0], output[i][1], IPs, RTs, 0, 1, 1]
      dataframe.append(input)

      for j in range(len(output)):
        # Same user
        last = len(dataframe) -1
        if (dataframe[last][1] == output[j][1]):
          # New Conection
          dataframe[last][4] += 1
          # If the IP associate is new append it in new table
          conf = False
          for k in range(len(dataframe[last][2])) :
            if (dataframe[last][2][k] == output[j][2]):
              conf = True
          
          if conf == False:
            dataframe[last][2].append(output[j][2])
            dataframe[last][5] += 1

          conf = False
          for k in range(len(dataframe[last][3])) :
            if (dataframe[last][3][k] == output[j][3]):
              conf = True
          
          if conf == False:
            dataframe[last][3].append(output[j][3])
            dataframe[last][6] += 1



  # 4. Cuántas conexiones por cada ruta se establecieron (mostrar un gráfico).
    # list of pairs (route, counter)
    # TODO: revisar que todo esta en orden 
    # WARNING: esta lista toda el proceso solo falta agregar la graficacion
  analyzer_conn = []
  analyzer_conn = analyzer.vpn_con()
  analyzer_vpns = []
  analyzer_vpns = analyzer.vpn_table()
  vpns = analyzer_vpns = [line[1] for line in analyzer_vpns]
  connection_list = []
  
  for item in vpns:
    new_vpn = item.replace("[","").replace("]","") # get rid of the [] simbols of the vpns
    input = [item, 0]
    connection_list.append(input)
    
  
  for connection in connection_list:
    benchmark = connection
    counter = 0
    for line in analyzer_conn:
      for vpn in line:
        if benchmark[0] == vpn:
          counter +=1
    benchmark[1] = counter

  print (connection_list)
  connection_vpns = [line[0] for line in connection_list]
  vpn_amount = [line[1] for line in connection_list]

  plt.figure(1,figsize=(8,6))
  plt.bar(connection_vpns,vpn_amount)# ,Poner colores)
  plt.title("Chart of usage of VPNs")
  plt.xlabel("VPN Used")
  plt.ylabel("Times")
  plt.grid(True,axis = 'y', color = 'g')
  plt.savefig('VPNs.png')
  
  # 5. Los 5 usuarios con más conexiones realizadas (mostrar un gráfico).
  # TODO: put this function in the new application code
  # vector with the names
  names = [line[1] for line in dataframe]
  # vector with the connections( treated as ints)
  conections = [int(conection[4]) for  conection in dataframe]
  # sort the names and conections 
  all_sort = sorted(list(zip(names,conections)), key=lambda x: x[1], reverse=True)
  nombres_ordenados , cantidades = zip(*all_sort)
  
  # reduce the amount to the best 5
  name_top5 = nombres_ordenados[:5]
  amount_top5 = cantidades[:5]

  # Colors
  # Obtain from: https://www.webucator.com/article/python-color-constants-module/
  bars_colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#00FFFF', '#800080']
  # create the chart
  plt.figure(2,figsize=(8,6))
  plt.bar(name_top5, amount_top5, color = bars_colors)
  plt.title("Chart of users with more conections")
  plt.xlabel("Users")
  plt.ylabel("Connections per users")
  plt.grid(True,axis = 'y', color = 'b')
  
  plt.show()
  # TODO : some errors with the save
  plt.savefig('Connections_per_user.png')
  # end TODO -------------------------------------------------