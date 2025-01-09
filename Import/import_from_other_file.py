print('─'*70)
import __fileTOexport as fte          # As we have imported the complete file, hence the call (to welcome) which is already in the file would also be executed                                              
fte.welcome()
print(fte.ratinder)                                                        ; print('─'*70)

from __fileTOexport import ratinder      # import only variable 'ratinder'
print(ratinder)                                                            ; print('─'*70)

from __fileTOexport import welcome      # import only function welcome()
welcome()                                                                  ; print('─'*70)

from __fileTOexport import welcome, ratinder
welcome()
print(ratinder)                                                            ; print('─'*70)