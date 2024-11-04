value = int(input("Menu:\n1.\tPhone book\n2.\tMessages\n3.\tChat\n4.\tCall register\n5.\tTones\n6.\tSettings\n7.\tCall divert\n8.\tGames\n9.\tCalculator\n10.\tReminders\n11.\tClock\n12.\tProfiles\n13.\tSIM services\n>>>> "))
match value:
    case 1:
        value = int(input("Phone book: \n1.\tSearch\n2.\tService Nos.\n3.\tAdd name\n4.\tErase\n5.\tEdit\n6.\tAssign tone\n7.\tSend b'card\n8.\tOption\n9.\tSpeed dials\n10.\tVoice tags\n>>>> "))
        match value:
            case 1:print("Search")
            case 2:print("Service Nos.")
            case 3:print("Add name")
            case 4:print("Erase")
            case 5:print("Edit")
            case 6:print("Assign tone")
            case 7:print("Send b\'card")
            case 8:
                value = int(input("Options:\n1.\tType of view\n2.\tMemory status\n>>>> "))
                match value:
                    case 1:print("Type of view:")
                    case 2:print("Memory status:")
            case 9:print("Speed dials")
            case 10:print("Voice tags")
    case 2:
        value = int(input("Messages:\n1.\tWrite messages\n2.\tInbox\n3.\tOutbox\n4.\tPicture messages\n5.\tTemplates\n6.\tSmileys\n7.\tMessage settings\n8.\tInfo service\n9.\tVoice mailbox number\n10.\tService command editor\n>>>> "))
        match value:
            case 1:print("Write messages")
            case 2:print("Inbox")
            case 3:print("Outbox")
            case 4:print("Picture messages")
            case 5:print("Templates")
            case 6:print("Smileys")
            case 7:
                value = int(input("Message settings:\n1.\tSet 1\n2.\tCommon\n>>>> "))
                match value:
                    case 1:
                        value = int(input("Set 1:\n1.\tMessage centre number\n2.\tMessages sent as\n3.\tMessage validity\n>>>> "))
                        match value:
                            case 1:print("Message centre number")
                            case 2:print("Messages sent as")
                            case 3:print("Message validity")
                    case 2:
                        value = int(input("Common:\n1.\tDelivery reports\n2.\tReply via same centre\n3.\tCharacter support\n>>>> "))
                        match value:
                            case 1:print("Delivery reports")
                            case 2:print("Reply via same centre")
                            case 3:print("Character support")
            case 8:print("Info service")
            case 9:print("Voice mailbox number")
            case 10:print("Service command editor")
    case 3:print("Chat")#chat
    case 4:#call register
        value = int(input("Call register:\n1.\tMissed calls\n2.\tReceived calls\n3.\tDialled numbers\n4.\tErase recent call lists\n5.\tShow call duration\n6.\tShow call costs\n7.\tCall cost settings\n8.\tPrepaid credit\n>>>> "))
        match value:
            case 1:print("Missed calls")
            case 2:print("Received calls")
            case 3:print("Dialled numbers")
            case 4:print("Erase recent call lists")
            case 5:
                value = int(input("Show call duration:\n1.\tLast call duration\n2.\tAll calls\' duration\n3.\tReceived calls\' duration\n4.\tDialled calls\' duration\n5.\tClear timers\n>>>> "))
                match value:
                    case 1:print("Last call duration")
                    case 2:print("All calls\' duration")
                    case 3:print("Received calls\' duration")
                    case 4:print("Dialled calls\' duration")
                    case 5:print("Clear timers")
            case 6:
                value = int(input("Show call costs:\n1.\tLast call cost\n2.\tAll calls\' cost\n3.\tClear counters\n>>>> "))
                match value:
                    case 1:print("Last call cost")
                    case 2:print("All calls\' cost")
                    case 3:print("Clear counters")
            case 7:
                value = int(input("Call cost settings:\n1.\tCall cost limit\n2.\tShow costs in\n>>>> "))
                match value:
                    case 1:print("Call cost limit")
                    case 2:print("Show costs in")
            case 8:print("Prepaid credit")#Prepaid credit
    case 5:
        value = int(input("Tones:\n1.\tRinging tone\n2.\tRinging volume\n3.\tIncoming call alert\n4.\tComposer\n5.\tMessage alert tone\n6.\tKeypad tones\n7.\tWarning and game tones\n8.\tVibrating alert\n9.\tScreen saver\n>>>> "))
        match value:
            case 1:print("Ringing tone")
            case 2:print("Ringing volume")
            case 3:print("Incoming call alert")
            case 4:print("Composer")
            case 5:print("Message alert tone")
            case 6:print("Keypad tones")
            case 7:print("Warning and game tones")
            case 8:print("Vibrating alert")
            case 9:print("Screen saver")
    case 6:
        value = int(input("Settings:\n1.\tCall settings\n2.\tPhone settings\n3.\tSecurity settings\n4.\tComposer\n>>>> "))
        match value:
            case 1:
                value = int(input("Call settings:\n1.\tAutomatic redial\n2.\tSpeed dialling\n3.\tCall waiting options\n4.\tOwn number sending\n5.\tPhone line in use\n6.\tAutomatic answer\n>>>> "))
                match value:
                    case 1:print("Automatic redial")
                    case 2:print("Speed dialling")
                    case 3:print("Call waiting options")
                    case 4:print("Own number sending")
                    case 5:print("Phone line in use")
                    case 6:print("Automatic answer")
            case 2:
                value = int(input("Phone settings:\n1.\tLanguage\n2.\tCell info display\n3.\tWelcome note\n4.\tNetwork selection\n5.\tLights\n6.\tConfirm SIM service actions\n>>>> "))
                match value:
                    case 1:print("Language")
                    case 2:print("Cell info display")
                    case 3:print("Welcome note")
                    case 4:print("Network selection")
                    case 5:print("Lights")
                    case 6:print("Confirm SIM service actions")
            case 3:
                value = int(input("Security settings:\n1.\tPIN code request\n2.\tCall barring service\n3.\tFixed dialling\n4.\tClosed user group\n5.\tPhone security\n6.\tChange access codes\n>>>> "))
                match value:
                    case 1:print("PIN code request")
                    case 2:print("Call barring service")
                    case 3:print("Fixed dialling")
                    case 4:print("Closed user group")
                    case 5:print("Phone security")
                    case 6:print("Change access codes")
            case 4:print("Restore factory settings")#Restore factory settings
                
    case 7:print("Call divert")
    case 8:print("Games")
    case 9:print("Calculator")
    case 10:print("Reminders")
    case 11:
        value = int(input("Clock:\n1.\tAlarm clock\n2.\tClock settings\n3.\tDate setting\n4.\tStopwatch\n5.\tCountdown timer\n6.\tAuto update of date and time\n>>>> "))
        match value:
            case 1:print("Alarm clock")
            case 2:print("Clock settings")
            case 3:print("Date setting")
            case 4:print("Stopwatch")
            case 5:print("Countdown timer")
            case 6:print("Auto update of date and time")
    case 12:print("Profiles")
    case 13:print("SIM services")
