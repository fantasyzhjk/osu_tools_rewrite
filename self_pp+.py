import package.info


def pp_plus_out(input):
    out = ('-------------------------------------------------------\n'
           '玩家{UserName}的pp+数据如下\n\n'
           'Total:      {PerformanceTotal:.2f}\n'
           'Aim:        {AimTotal:.2f}\n'
           'Jump:       {JumpAimTotal:.2f}\n'
           'Flow:       {FlowAimTotal:.2f}\n'
           'Precision:  {PrecisionTotal:.2f}\n'
           'Speed:      {SpeedTotal:.2f}\n'
           'Stamina:    {StaminaTotal:.2f}\n'
           'Accuracy:   {AccuracyTotal:.2f}\n'
           '-------------------------------------------------------').format(**input)
    return out


if __name__ == "__main__":
    pp_plus_json = package.info.get_self_pp_plus()
    print(pp_plus_out(pp_plus_json))
    input()
