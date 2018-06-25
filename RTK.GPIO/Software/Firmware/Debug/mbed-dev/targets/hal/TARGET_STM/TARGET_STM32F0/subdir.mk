################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogin_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogout_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_irq_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/i2c_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/mbed_overrides.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pinmap.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/port_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pwmout_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/rtc_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/serial_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/sleep.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/spi_api.c \
../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/us_ticker.c 

OBJS += \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogin_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogout_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_irq_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/i2c_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/mbed_overrides.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pinmap.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/port_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pwmout_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/rtc_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/serial_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/sleep.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/spi_api.o \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/us_ticker.o 

C_DEPS += \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogin_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/analogout_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/gpio_irq_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/i2c_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/mbed_overrides.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pinmap.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/port_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/pwmout_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/rtc_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/serial_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/sleep.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/spi_api.d \
./mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/us_ticker.d 


# Each subdirectory must supply rules for building sources it contributes
mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/%.o: ../mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU GCC Compiler'
	@echo $(PWD)
	arm-none-eabi-gcc -mcpu=cortex-m0 -mthumb -mfloat-abi=soft -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTINOUT=1 -D__MBED_CMSIS_RTOS_CM -DTARGET_STM32F0 -DDEVICE_RTC=1 -DTOOLCHAIN_object -DTARGET_NUCLEO_F030R8 -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DTARGET_CORTEX_M -DARM_MATH_CM0 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_M0 -DDEVICE_SERIAL=1 -DDEVICE_INTERRUPTIN=1 -D__CORTEX_M0 -DDEVICE_I2C=1 -DDEVICE_PORTOUT=1 -DDEVICE_STDIO_MESSAGES=1 -DMBED_BUILD_TIMESTAMP=1473017828.47 -DTARGET_FF_MORPHO -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DTARGET_RELEASE -DTARGET_STM -DDEVICE_PORTIN=1 -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_SPI=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_STM32F030R8 -DTARGET_LIKE_CORTEX_M0 -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/." -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/SoftPWM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/api" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/hal/storage_abstraction" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/cmsis/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8/TOOLCHAIN_GCC_ARM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/targets/hal/TARGET_STM/TARGET_STM32F0/TARGET_NUCLEO_F030R8" -I"/Users/ryanwalmsley/Documents/workspace/RTkGPIO-V1/mbed-dev/common" -Og -g3 -Wall -fmessage-length=0 -ffunction-sections -c -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


